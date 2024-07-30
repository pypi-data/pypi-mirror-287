from pathlib import Path

from PIL import Image
from loguru import logger

import pcleaner.image_ops as ops
import pcleaner.structures as st


def denoise_page(d_data: st.DenoiserData) -> st.DenoiseAnalytic:
    """
    Load the MaskData from the json file and perform the denoising process.

    :param d_data: All the data needed for the denoising process.
    :return: Analytics.
    """
    # Load all the cached data.
    mask_data = st.MaskData.from_json(d_data.json_path.read_text(encoding="utf-8"))
    mask_image = Image.open(mask_data.mask_path)

    # Clobber protection prefixes have the form "{UUID}_file name", ex. d91d86d1-b8d2-400b-98b2-2d0337973631_0023.json
    clobber_protection_prefix = d_data.json_path.stem.split("_")[0]
    cache_out_path = (
        d_data.cache_dir
        / f"{clobber_protection_prefix}_{mask_data.original_path.with_suffix('.png').name}"
    )

    def save_mask(img, name_suffix, force: bool = False) -> None:
        if d_data.show_masks or force:
            img.save(cache_out_path.with_stem(cache_out_path.stem + name_suffix))

    # Scale the mask to the original image size, if needed.
    cleaned_image = Image.open(mask_data.original_path)
    mask_image = mask_image.convert("LA")
    cleaned_image = cleaned_image.convert("RGB")
    scale_up_factor = 1.0
    if cleaned_image.size != mask_image.size:
        scale_up_factor = cleaned_image.size[0] / mask_image.size[0]
        mask_image = mask_image.resize(cleaned_image.size, resample=Image.NEAREST)

    cleaned_image.paste(mask_image, (0, 0), mask_image)
    original_path: Path = mask_data.original_path

    # Alias.
    g_conf = d_data.general_config
    d_conf = d_data.denoiser_config
    i_conf = d_data.inpainter_config

    # Filter for the min deviation to consider for denoising.
    boxes_to_denoise: list[st.Box] = [
        box
        for box, deviation, failed, _ in mask_data.boxes_with_stats
        if not failed and deviation > d_conf.noise_min_standard_deviation
    ]

    noise_masks_with_coords: list[tuple[Image.Image, tuple[int, int]]] = [
        ops.generate_noise_mask(cleaned_image, mask_image, box, d_conf, scale_up_factor)
        for box in boxes_to_denoise
    ]

    if noise_masks_with_coords:
        combined_noise_mask = ops.combine_noise_masks(cleaned_image.size, noise_masks_with_coords)
        cleaned_image.paste(combined_noise_mask, (0, 0), combined_noise_mask)
    else:
        # noinspection PyTypeChecker
        combined_noise_mask = Image.new("LA", cleaned_image.size, (0, 0))

    # If inpainting, we need the noise mask either way.
    save_mask(combined_noise_mask, "_noise_mask", force=i_conf.inpainting_enabled)
    save_mask(cleaned_image, "_clean_denoised")

    # Check if the output path is None. In that case we're only outputting to the cache directory.
    if d_data.output_dir is None:
        # # Check if we still need to output the isolated text, otherwise we're done.
        # if d_data.extract_text:
        #     # Extract the text layer from the image.
        #     logger.debug(f"Extracting text from {original_path}")
        #     base_image = Image.open(original_path)
        #     text_img = ops.extract_text(base_image, mask_image)
        #     save_mask(text_img, "_text")
        #
        # Package the analytics. We're only interested in the std deviations.
        return st.DenoiseAnalytic(
            tuple(deviation for _, deviation, _, _ in mask_data.boxes_with_stats), original_path
        )

    # Settle on the final output path for the cleaned image.
    if d_data.output_dir.is_absolute():
        final_out_path = d_data.output_dir / mask_data.target_path.name
    else:
        # Take the original image path, and place the image in a subdirectory.
        # This is for when multiple directories were passed in.
        final_out_path = (
            mask_data.target_path.parent / d_data.output_dir / mask_data.target_path.name
        )

    final_out_path.parent.mkdir(parents=True, exist_ok=True)
    final_cleaned_out_path = final_out_path.with_name(final_out_path.stem + "_clean.png")
    final_mask_out_path = final_out_path.with_name(final_out_path.stem + "_mask.png")
    final_mask_denoised_out_path = final_out_path.with_name(
        final_out_path.stem + "_denoised_mask.png"
    )

    # Check what the preferred output format is.
    if g_conf.preferred_file_type is None:
        # Use the original file type.
        final_cleaned_out_path = final_cleaned_out_path.with_suffix(original_path.suffix)
    else:
        final_cleaned_out_path = final_cleaned_out_path.with_suffix(g_conf.preferred_file_type)

    if g_conf.preferred_mask_file_type is None:
        # Use png by default.
        final_mask_out_path = final_mask_out_path.with_suffix(".png")
    else:
        final_mask_out_path = final_mask_out_path.with_suffix(g_conf.preferred_mask_file_type)

    # The arg parser should ensure that both can't be true at once, not like that'd be an issue, just plain silly.
    if not d_data.save_only_mask:
        # Save the final image.
        logger.debug(f"Saving final image to {final_cleaned_out_path}")
        ops.save_optimized(cleaned_image, final_cleaned_out_path, original_path)

    if not d_data.save_only_cleaned:
        # Save the final image.
        if d_data.separate_noise_masks:
            logger.debug(f"Saving final mask to {final_mask_out_path}")
            ops.save_optimized(mask_image, final_mask_out_path)

            logger.debug(f"Saving final denoised mask to {final_mask_denoised_out_path}")
            ops.save_optimized(combined_noise_mask, final_mask_denoised_out_path)
        else:
            # Combine both the mask and the denoised mask into one image.
            combined_noise_mask.paste(mask_image, (0, 0), mask_image)
            logger.debug(f"Saving final mask to {final_mask_out_path}")
            ops.save_optimized(combined_noise_mask, final_mask_out_path)

    if d_data.extract_text:
        # Extract the text layer from the image.
        logger.debug(f"Extracting text from {original_path}")
        base_image = Image.open(original_path)
        text_img = ops.extract_text(base_image, mask_image)
        text_out_path = final_out_path.with_name(final_out_path.stem + "_text.png")
        if g_conf.preferred_mask_file_type is None:
            # Use png by default.
            text_out_path = text_out_path.with_suffix(".png")
        else:
            text_out_path = text_out_path.with_suffix(g_conf.preferred_mask_file_type)
        ops.save_optimized(text_img, text_out_path, original_path)

    # Package the analytics. We're only interested in the std deviations.
    return st.DenoiseAnalytic(
        tuple(deviation for _, deviation, _, _ in mask_data.boxes_with_stats), original_path
    )

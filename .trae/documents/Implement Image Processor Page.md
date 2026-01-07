# Create Image Processor Tool

## 1. Create `image-processor.html`
- **Layout Structure**:
  - Replicate the header and navigation style from existing tools.
  - Implement the two-column layout:
    - **Left Column**:
      - **Upload Section**: Drag & drop zone, file input, format warnings.
      - **Preview Area**: Canvas or Image element to show the current state.
      - **Resize Section**: Width/Height inputs with aspect ratio lock options, Zoom controls.
      - **Crop Section**: Preset buttons (1-inch, 2-inch, etc.) and custom dimension inputs.
      - **Compress Section**: Target file size input (KB).
      - **Download Section**: Download button and QR code placeholder.
    - **Right Column**:
      - **About Section**: Tool description and specs.
      - **Related Tools**: Links to "Background Remover", "Image Converter", etc. (UI only).
      - **Developer API**: Blue call-to-action card.
- **Styling**:
  - Use Tailwind CSS to match the provided design (colors, spacing, shadows).
  - Ensure responsive behavior (stacking columns on mobile).

## 2. Implement Image Processing Logic (Vanilla JS)
- **File Handling**: `FileReader` to load images.
- **Core Processing**:
  - Use HTML5 `<canvas>` for resizing and cropping.
  - Implement `toDataURL` with quality parameters for compression.
- **Interactions**:
  - Real-time preview updates.
  - "Confirm Modification" buttons to apply changes to the source image (or update preview).
  - Download functionality using a temporary anchor tag.

## 3. Update `index.html`
- Add "Image Processor" to the tools grid.
- Use a suitable icon (e.g., `fa-image` or `fa-wand-magic`).
- Ensure it filters correctly under "Design" or "Productivity" categories.

## 4. Verification
- Check responsiveness.
- Verify image loading and processing (resize, compress).
- Ensure visual consistency with the provided screenshot.

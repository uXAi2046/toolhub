# 汉化处理计划：图片处理器 (Image Processor)

通过分析项目结构，我发现目前的汉化策略是采用“一语一文件”的方式（如 `tool.html` 对应 `tool-zh.html`）。目前 `image-processor.html` 尚未进行汉化。

我将按照以下步骤完成该工具页面的汉化：

## 1. 创建中文版文件
- **复制文件**：基于 `image-processor.html` 创建 `image-processor-zh.html`。

## 2. 实施汉化内容
我们将翻译界面上的所有可见文本，包括：
- **页面标题与描述**：
  - "Image Processor" -> "图片处理器"
  - 功能描述翻译为中文（修改尺寸、裁剪、压缩、证件照制作等）。
- **功能模块**：
  - **上传区**："Upload Image" -> "上传图片"，及相关提示（支持格式、大小限制）。
  - **尺寸修改**："Resize Image" -> "修改尺寸"，"Width/Height" -> "宽度/高度"，"Zoom" -> "缩放"。
  - **裁剪/比例**："Change Dimensions (Crop)" -> "修改比例/裁剪"，预设按钮（1寸、2寸、正方形等）。
  - **压缩**："Compress File Size" -> "压缩文件大小"，"Target Size" -> "目标大小"。
  - **下载**："Save / Download" -> "保存/下载"，"Desktop/Mobile" -> "电脑端/移动端"。
- **侧边栏**：
  - "About this tool" -> "关于此工具"。
  - "Related Tools" -> "相关工具"（并将链接指向对应的 `-zh.html` 版本）。
  - "Developer API" -> "开发者 API"。
- **交互反馈**：
  - 将 JavaScript 中的 `alert` 和 `showToast` 提示信息翻译为中文（如 "File size exceeds 5MB" -> "文件大小超过 5MB"）。

## 3. 添加语言切换导航
为了方便用户在双语间切换，我将修改两个文件的头部：
- **英文版 (`image-processor.html`)**：在顶部导航栏添加 "中文" 切换按钮，指向 `image-processor-zh.html`。
- **中文版 (`image-processor-zh.html`)**：在顶部导航栏添加 "EN" 切换按钮，指向 `image-processor.html`。

## 4. 验证
- 确认中文版页面显示正常，无乱码。
- 确认所有功能（上传、处理、下载）在中文版中依然可用。
- 确认双语切换链接跳转正确。

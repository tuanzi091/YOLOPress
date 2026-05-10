# CLIPasso - 在 Google Colab 上运行

## 最简单的方法：使用 Google Colab

由于在Windows上安装这个项目需要编译C++代码（diffvg）和下载大型模型（PyTorch 1.2GB），**强烈推荐使用Google Colab**。

### 步骤：

1. **打开 Google Colab**
   - 访问 https://colab.research.google.com
   - 上传 `CLIPasso.ipynb` 文件（项目根目录有提供）

2. **或者直接访问 Colab 链接**
   - 项目提供了直接运行链接：https://colab.research.google.com/github/yael-vinker/CLIPasso/blob/main/CLIPasso.ipynb

3. **在 Colab 中运行**
   - 点击 "Runtime" → "Run all"
   - 或者按 Ctrl+F9

4. **上传你的图片**
   - 在notebook中找到上传部分
   - 上传你想转换成草图的图片

5. **下载结果**
   - 生成的SVG文件可以直接下载

## Colab 的优势

✅ **无需安装** - 所有依赖都已配置好
✅ **免费GPU** - 使用Google的Tesla T4 GPU
✅ **快速运行** - 完整的2000次迭代只需约10-15分钟
✅ **无需CUDA配置** - Google已处理好所有驱动

## 在本地 Windows 运行（复杂）

如果你仍想在本地运行，请参考 `WINDOWS_INSTALLATION_GUIDE.md` 文件。

**主要挑战**：
1. diffvg 需要 C++ 编译环境（Visual Studio Build Tools）
2. PyTorch 1.7.1 需要 CUDA 10.1（你的系统是 13.2）
3. 网络下载经常超时
4. 某些依赖包版本冲突

## 推荐的本地运行配置

如果你决定继续本地安装，建议：
- 使用 Anaconda 管理环境
- 安装 CUDA 10.1 工具链
- 分配至少50GB磁盘空间
- 确保稳定的网络连接
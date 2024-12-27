# English to Chinese Translation App

一个基于 Gradio 的英文到中文翻译应用，使用 DRT-o1-7B 大语言模型进行高质量翻译。

## 功能特点

- 支持上传 TXT 文件进行批量翻译
- 智能分段翻译，保持上下文连贯性
- 实时显示翻译进度
- 优化的输出格式，直接展示翻译结果
- 支持长文本翻译

## 安装要求

- Python 3.8+
- PyTorch
- Transformers
- Gradio

## 快速开始

1. 克隆仓库：

```bash
git clone [your-repository-url]
cd [repository-name]
```

1. 安装依赖：

```
pip install -r requirements.txt
```

1. 下载模型文件： 确保 DRT-o1-7B 模型文件位于项目根目录下的 `DRT-o1-7B` 文件夹中。
2. 运行应用：

```
python app.py
```

1. 在浏览器中访问： 默认情况下，应用会在 http://localhost:7860 启动

## 使用方法

1. 打开应用后，点击上传按钮选择要翻译的 TXT 文件
2. 等待翻译完成，进度条会显示当前翻译进度
3. 翻译完成后，结果会自动显示在界面上

## 项目结构

```
.
├── README.md
├── app.py                 # 主应用程序
└── DRT-o1-7B/            # 模型文件夹
```

## 技术细节

- 使用 Gradio 构建用户界面
- 基于 DRT-o1-7B 大语言模型进行翻译
- 实现了文本分段处理，优化长文本翻译效果
- 使用正则表达式提取并优化翻译输出

## License

MIT License

## 贡献

欢迎提交 Issues 和 Pull Requests！

## 致谢

- Gradio 团队提供的优秀 UI 框架
- DRT-o1-7B 模型的开发团队
 

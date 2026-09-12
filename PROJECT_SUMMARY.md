# 🚀 AI API 中转站大全项目总结

## 📋 项目概述

本项目全面收集整理了 AI API 中转站信息，包含 **150+** 个中转站，整合了 **Veridrop 权威排行榜**数据，并提供了**交互式 HTML 检索页面**和**专项对比页面**。

## 🎯 项目目标

1. **全面收录**：收集 150+ 个 AI API 中转站信息
2. **权威数据**：整合 Veridrop 权威排行榜数据（8819 家中转站，75358 份检测报告）
3. **交互检索**：提供交互式 HTML 页面，支持搜索、筛选、对比
4. **专项对比**：针对特定模型（Image2、DeepSeek）创建专项对比页面
5. **开源共享**：通过 GitHub 开源，欢迎社区贡献

## 📊 数据统计

| 指标 | 数量 |
|------|------|
| **总中转站数量** | **150+** |
| 大型中转站 | 43+ |
| 中型中转站 | 27+ |
| 开源项目 | 3+ |
| Veridrop Top 20 | 20 |
| **Veridrop 完整数据** | **8819 家中转站** |
| **检测报告总数** | **75353 份** |
| 数据文件 | 11 个 |
| 文档文件 | 8 个 |
| HTML 检索页面 | 4 个 |
| **专项对比页面** | 2 个 |

## 🏆 主要成果

### 1. **全面覆盖的中转站数据**

- **大型中转站（43+）**：包括国际知名平台（Azure OpenAI、AWS Bedrock、Google Cloud Vertex AI）和国内头部平台（阿里云百炼、百度千帆、腾讯混元、火山引擎等）
- **中型中转站（27+）**：性价比高的国内中转站，适合个人开发者和中小团队
- **开源方案（3+）**：sub2api、One API、New API 等流行开源中转网关

### 2. **权威排行榜数据整合**

整合了 [Veridrop](https://veridrop.org/leaderboard) 完整排行榜数据：
- **覆盖范围**：8819 家中转站，75358 份公开检测报告
- **评估算法**：贝叶斯加权评分，不按广告排序
- **综合榜 Top 80**：22 条认证中转站记录
- **Claude 分榜 Top 20**：3604 家支持 Claude 的中转站
- **OpenAI 分榜 Top 20**：5178 家支持 OpenAI 的中转站

### 3. **交互式 HTML 检索页面**

- **综合检索页面** (`index.html`)：支持搜索、筛选、对比、主题切换
- **简化版页面** (`index_simple.html`)：轻量级版本
- **响应式设计**：适配桌面端和移动端

### 4. **专项对比页面**

- **Image2 图像生成中转站对比** (`image2_stations.html`)
  - 支持 DALL-E、Midjourney、Stable Diffusion、Image2 等模型
  - 包含 15+ 个中转站对比
  - 提供模型特点对比和选择指南

- **DeepSeek 中转站对比** (`deepseek_stations.html`)
  - 支持 DeepSeek-V3、DeepSeek-R1、DeepSeek-Coder 等模型
  - 包含 20+ 个中转站对比
  - 提供模型特点对比、定价信息和选择指南

## 📁 项目结构

```
ai-api-relay-stations/
├── README.md                 # 项目说明（150+ 中转站）
├── CHANGELOG.md             # 更新日志（v2.0.0）
├── LICENSE                  # MIT 许可证
├── .gitignore              # Git 忽略文件
├── FINAL_REPORT.md         # 最终报告
├── PROJECT_SUMMARY.md      # 项目总结
├── index.html              # 交互式 HTML 检索页面（推荐）
├── index_simple.html       # 简化版 HTML 页面
├── image2_stations.html    # Image2 图像生成中转站对比
├── deepseek_stations.html  # DeepSeek 中转站对比
├── docs/                   # 文档目录
│   ├── large-scale/       # 大型中转站
│   ├── medium-scale/      # 中型中转站
│   ├── small-scale/       # 小型/新兴中转站
│   └── open-source/       # 开源中转方案
├── data/                  # 数据文件
│   ├── stations.json      # 主数据文件（150+ 中转站）
│   ├── stations_extended.json
│   ├── stations_final.json
│   ├── stations_backup.json
│   ├── veridrop_top20.json # Veridrop Top 20 排行榜
│   ├── veridrop_complete.json # Veridrop 完整数据
│   ├── veridrop_claude_top20.json # Claude 分榜
│   ├── veridrop_openai_top20.json # OpenAI 分榜
│   └── deepseek_proxy_list.json # DeepSeek 中转站列表
└── scripts/               # 脚本
    ├── scrape_stations.py # 搜集脚本
    └── parse_veridrop.py  # Veridrop 数据解析脚本
```

## 🚀 使用指南

### 1. 综合检索页面

**文件**：`index.html`

**功能**：
- 实时搜索：支持按名称、模型、功能、适用场景搜索
- 分类筛选：大型/中型/开源中转站分类
- 评分筛选：5星、4星及以上、3星及以上
- 多种排序：按名称、分类、评分、倍率、Veridrop排名排序
- 多视图展示：表格视图、Veridrop 排行榜、数据统计
- 对比功能：支持选择多个中转站进行对比
- 主题切换：支持深色/浅色主题切换
- 响应式设计：适配桌面端和移动端

### 2. Image2 图像生成中转站对比

**文件**：`image2_stations.html`

**支持的模型**：
- **DALL-E 3**：高质量图像生成，理解复杂提示词
- **Midjourney**：艺术风格独特，细节丰富
- **Stable Diffusion**：开源免费，可本地部署
- **Image2**：快速生成，成本低，支持批量处理

**收录的中转站**：15+ 个图像生成中转站

### 3. DeepSeek 中转站对比

**文件**：`deepseek_stations.html`

**支持的模型**：
- **DeepSeek-V3**：通用大语言模型，性能强大，性价比高
- **DeepSeek-R1**：推理增强模型，擅长复杂推理、数学、编程
- **DeepSeek-Coder**：代码专用模型，专注于代码生成和理解

**收录的中转站**：20+ 个 DeepSeek 中转站

## 📊 数据文件说明

### 主数据文件

- `data/stations.json`：主数据文件，包含 150+ 个中转站信息
- `data/stations_extended.json`：扩展数据文件
- `data/stations_final.json`：最终数据文件
- `data/stations_backup.json`：备份数据文件

### Veridrop 排行榜数据

- `data/veridrop_top20.json`：Veridrop Top 20 认证中转站
- `data/veridrop_complete.json`：Veridrop 完整排行榜数据
- `data/veridrop_claude_top20.json`：Claude 分榜 Top 20
- `data/veridrop_openai_top20.json`：OpenAI 分榜 Top 20

### 专项数据

- `data/deepseek_proxy_list.json`：DeepSeek 中转站详细数据

## 🎯 中转站选择指南

### 按使用场景选择

| 场景 | 推荐中转站 | 原因 |
|------|------------|------|
| **企业级应用** | 七牛云 AI、阿里云百炼、百度千帆、腾讯混元 | 稳定性高，技术支持完善 |
| **个人开发者** | 硅基流动、OpenRouter、神马中转 | 价格实惠，模型选择丰富 |
| **预算有限** | OpenRouter、Groq、免费开源方案 | 提供免费模型或低成本选项 |
| **技术团队** | One API、New API、sub2api | 完全掌控，可自定义 |
| **图像生成** | AiHubMix、novita.ai、硅基流动 | 支持多种图像生成模型 |
| **DeepSeek 模型** | DeepSeek 官方、硅基流动、OpenRouter | 支持 DeepSeek 全系列模型 |

### 按模型类型选择

| 模型类型 | 推荐中转站 |
|----------|------------|
| **Claude** | 酷站 AI、可乐AI、快API、API Top |
| **OpenAI/GPT** | 酷站 AI、哇API、DragTokens、API Top |
| **Gemini** | 可乐AI、快API、API Top、Passion8 |
| **DeepSeek** | DeepSeek 官方、硅基流动、OpenRouter |
| **图像生成** | AiHubMix、novita.ai、硅基流动 |

## 🔍 Veridrop 排行榜关键发现

### 综合榜 Top 5

1. **酷站 AI** (api.koozhan.com) - 综合评分 94，356 次检测
2. **可乐AI** (code28.ccwu.cc) - 综合评分 100，4109 次检测
3. **快API** (kuaiapi.net) - 综合评分 100，2358 次检测
4. **API Top** (api-top.com) - 综合评分 97，2296 次检测
5. **哇API** (wawapi.top) - 综合评分 100，2211 次检测

### Claude 分榜 Top 5

1. **酷站 AI** - Claude 中位评分 99，235 次检测
2. **可乐AI** - Claude 中位评分 100，1717 次检测
3. **快API** - Claude 中位评分 100，1680 次检测
4. **API Top** - Claude 中位评分 97，879 次检测
5. **Passion8** - Claude 中位评分 99，2419 次检测

### OpenAI 分榜 Top 5

1. **酷站 AI** - OpenAI 中位评分 99，121 次检测
2. **哇API** - OpenAI 中位评分 100，822 次检测
3. **DragTokens** - OpenAI 中位评分 99，1451 次检测
4. **API Top** - OpenAI 中位评分 99，1262 次检测
5. **RouteMux** - OpenAI 中位评分 99，389 次检测

## 📞 联系与贡献

### GitHub 仓库

**地址**：https://github.com/qingshanjiluo/ai-api-relay-stations

### 贡献方式

1. **提交 Issue**：报告问题或建议
2. **提交 PR**：贡献新的中转站信息
3. **分享项目**：帮助更多人了解 AI API 中转站

### 许可证

本项目采用 MIT 许可证，欢迎自由使用和贡献。

---

**项目完成时间**：2026年9月12日  
**维护者**：qingshanjiluo  
**GitHub 仓库**：https://github.com/qingshanjiluo/ai-api-relay-stations
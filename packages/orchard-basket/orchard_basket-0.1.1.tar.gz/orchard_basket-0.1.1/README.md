# Basket

## Introduction

Basket is the essential toolkit for seamless MaaS integration.

It provides a unified interface for interacting with different MaaS services, allowing developers to easily switch between different services without changing their code. It is the first free toolkit that allows developers to use LLM services without registering or paying for them. Know more about [FreeModel](https://github.com/OrchardUniverse/FreeModel).

- Fast and free to access Model as a Service
- Unified interface for interacting with different MaaS services
- Easy to use and integrate with existing projects
- Manage API KEY for MaaS and easy to switch
- Extensible and customizable for local and remote services
- One step to chat with LLM service without coding and configurating

Refer to more [documentation](https://orchardai.github.io/basket/).


## Install

```
pip install orchard-basket
```

## Usage

1. Chat with FreeModel.

```
basket chat "Who are you"
```

2. List all available MaaS.

```
basket maas list
```

3. Choose the MaaS to use.

```
basket maas use siliconflow
```

4. List all available models.

```
basket model list
```

5. Choose the model to use.

```
basket model use qwen/qwen-7b-chat
```

6. Chat with the model.

```
basket chat "What is the meaning of life?"
```

8. Show current configuration.

```
basket config
```

## Contribution

Please help us to integrate with more MaaS.

- [x] [FreeModel](https://github.com/OrchardUniverse/FreeModel)
- [x] [OpenAI](https://platform.openai.com/)
- [x] [SiliconFlow](https://siliconflow.cn/siliconcloud)
- [x] [DashScope](https://dashscope.aliyun.com/)
- [x] [OpenRouter](https://openrouter.ai/)
- [x] [DeepSeek](https://platform.deepseek.com/)
- [x] [MoonShot](https://platform.moonshot.cn/)
- [x] [ZhiPu](https://maas.aminer.cn/)
- [x] [Lime](https://github.com/OrchardUniverse/lime)

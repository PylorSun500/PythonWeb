"""
配置文件
======
集中管理API密钥、大模型参数等。
实际部署时，敏感信息应从环境变量读取，切勿硬编码提交到Git仓库。

使用方式：
    from config import AIConfig
    api_key = AIConfig.API_KEY
"""

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    JSON_AS_ASCII = False  # 确保中文在JSON响应中正常显示
    DEBUG = True  # 开发模式，生产环境请关闭

class AIConfig:
    """
        大模型API配置
        ==============
        以DeepSeek为例（国产大模型，兼容OpenAI接口格式）。
        如需切换其他国产模型（通义千问/文心一言等），只需修改 BASE_URL 和 MODEL_NAME。

        获取DeepSeek API密钥：https://platform.deepseek.com/
    """
    # API密钥 —— 从环境变量读取，未设置时使用占位符
    API_KEY = os.environ.get('DEEPSEEK_API_KEY') or 'sk-34eec8826d754a5787b846b595d2711f'
    # API地址（DeepSeek兼容OpenAI的 /v1/chat/completions 格式）
    BASE_URL = 'https://api.deepseek.com/v1'
    # 模型名称
    MODEL_NAME = 'deepseek-chat'
    # 请求超时（秒）
    TIMEOUT = 30
    # 最大输出token数
    MAX_TOKENS = 1024
    # 温度参数（0~1，越高越有创造性，越低越严谨）
    TEMPERATURE = 0.7


# class AIConfig:
#     # 阿里云百炼API密钥（在百炼平台创建）
#     API_KEY = os.environ.get('DASHSCOPE_API_KEY') or 'your-api-key-here'
#
#     # 百炼兼容OpenAI接口的地址
#     BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
#
#     # 模型名称（Qwen3.5-Flash免费额度最充足）
#     MODEL_NAME = 'qwen3.5-flash'
#
#     TIMEOUT = 30
#     MAX_TOKENS = 1024
#     TEMPERATURE = 0.7


# class AIConfig:
#     API_KEY = 'sk-ydrmqiloberivwapexbinqdsowdpukiccxbjmmpprwvmbmbu'  # 你的硅基流动Key
#     BASE_URL = 'https://api.siliconflow.cn/v1'
#     MODEL_NAME = 'Qwen/Qwen2.5-7B-Instruct'  # 完全免费
#     TIMEOUT = 30
#     MAX_TOKENS = 1024
#     TEMPERATURE = 0.7
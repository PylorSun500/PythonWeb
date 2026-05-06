class Config:
    """
    配置类，用于存储应用程序的全局配置信息
    包含密钥、数据库连接等信息
    """
    # 设置密钥，用于加密和签名，确保应用安全性
    SECRET_KEY = 'jiangxi-water-culture-2026'
    # MySQL连接字符串，请修改为实际环境
    # 包含数据库类型(MySQL)、驱动(PyMySQL)、用户名(root)、密码(123456)、主机(localhost)、端口(3306)和数据库名(jiangxi_water_culture)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pylor520@localhost:3306/jiangxi_water_culture'
    # 禁用SQLAlchemy的信号系统，以减少内存使用
    SQLALCHEMY_TRACK_MODIFICATIONS = False
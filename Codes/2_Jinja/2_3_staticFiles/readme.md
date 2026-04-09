# 静态文件加载

[homepage.html](./templates/homepage.html)

css、js、媒体文件等静态文件也是一套网页中必不可少的构成内容。这些文件被叫做 **静态文件** 。
静态文件被放在 `res//static` 目录中。

参考 HTML 对 多媒体文件 或者 css 文件的引用语法，我们使用 [`url_for()`](../../1_1_Request_n_Response.ipynb) 函数引用静态文件的 URL 。

_e.g.__
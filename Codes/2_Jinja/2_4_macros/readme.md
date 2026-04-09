# 宏 `macro`

**宏** 是一个语句组。可复用，传参。无返回。

## 定义

```jinja2
{% macro name %}
    {# 代码段 #}
{% endmacro %}
```

## 使用

```jinja2
{{ name(args) }}
```

## 导入

宏可以被单独保存在 HTML 文件中被复用。这个 HTML 只拥有 `{% macro %}` - `{% endmacro %}` 内容，且遵循 Jinja2 的模板规则。

例如，创建一个 `calculate.html` 文件，其中写入名为 `add` 的 macro：

需要导入该文件时，在上方使用
```jinja2
{% from 'calculate.html' import add %}
```
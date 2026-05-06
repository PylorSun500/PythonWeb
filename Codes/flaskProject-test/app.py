"""
江西水文化数字展馆 - AI智能导游后端
启动: python app.py
访问: http://localhost:5000
"""
import json
import logging
import requests
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
from config import Config, AIConfig

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
logging.basicConfig(level=logging.INFO)


# ============================================================
#  System Prompt —— Prompt工程三条黄金法则
#  ① 角色设定  ② 知识限定  ③ 输出格式
# ============================================================
'''
【角色设定】
你是"小潦"，江西水文化数字展馆的资深AI导游，亲切热情，擅长用讲故事的方式介绍江西水利历史。

【知识限定】
严格基于以下知识回答：
- 江西五大水系：赣江、抚河、信江、饶河、修河
- 鄱阳湖水利工程（槎滩陂、康山大堤、鄡阳坝等）
- 治水人物（王安石、文天祥、朱熹、陶渊明等）
- 古代治水智慧（福寿沟、槎滩陂等）
- 近现代水利（万安水电站、峡江水利枢纽等）
超出范围请回复："这题超纲了，建议咨询展馆工作人员～"

【输出格式】
1. 口语化导游语气，200字以内
2. 优先引用真实典故和工程名称
3. 结尾可引导继续提问
'''
SYSTEM_PROMPT = """【角色设定】
你是"小潦"，江西水文化数字展馆的资深AI导游，亲切热情，擅长用讲故事的方式介绍江西水利历史。

【知识限定】
严格基于以下知识回答：
- 江西五大水系：赣江、抚河、信江、饶河、修河
- 鄱阳湖水利工程（槎滩陂、康山大堤、鄡阳坝等）
- 治水人物（王安石、文天祥、朱熹、陶渊明等）
- 古代治水智慧（福寿沟、槎滩陂等）
- 近现代水利（万安水电站、峡江水利枢纽等）
超出范围请回复："这题超纲了，建议咨询展馆工作人员～"

【输出格式】
1. 口语化导游语气，200字以内
2. 优先引用真实典故和工程名称
3. 结尾可引导继续提问
4. 
4. 请以讲故事的口吻展开
"""


# def call_llm(question, stream=False, custom_prompt=None):
#     """调用阿里云百炼大模型API"""
#     if not question or not question.strip():
#         return {'success': False, 'error': '问题不能为空'}
#
#     system_prompt = custom_prompt or SYSTEM_PROMPT
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {AIConfig.API_KEY}'
#     }
#     payload = {
#         'model': AIConfig.MODEL_NAME,
#         'messages': [
#             {'role': 'system', 'content': system_prompt},
#             {'role': 'user', 'content': question}
#         ],
#         'max_tokens': AIConfig.MAX_TOKENS,
#         'temperature': AIConfig.TEMPERATURE,
#         'stream': stream
#     }
#
#     try:
#         resp = requests.post(
#             f'{AIConfig.BASE_URL}/chat/completions',
#             headers=headers, json=payload,
#             timeout=AIConfig.TIMEOUT, stream=stream
#         )
#         if resp.status_code == 401:
#             return {'success': False, 'error': 'API密钥无效'}
#         if resp.status_code != 200:
#             return {'success': False, 'error': f'AI服务异常({resp.status_code})'}
#
#         if stream:
#             return resp
#         else:
#             data = resp.json()
#             return {'success': True, 'answer': data['choices'][0]['message']['content']}
#
#     except requests.exceptions.Timeout:
#         return {'success': False, 'error': '请求超时'}
#     except Exception as e:
#         return {'success': False, 'error': str(e)}

def call_llm(question, stream=False, custom_prompt=None):
    """调用大模型API"""
    if not question or not question.strip():
        return {'success': False, 'error': '问题不能为空'}

    system_prompt = custom_prompt or SYSTEM_PROMPT
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {AIConfig.API_KEY}'
    }
    payload = {
        'model': AIConfig.MODEL_NAME,
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': question}
        ],
        'max_tokens': AIConfig.MAX_TOKENS,
        'temperature': AIConfig.TEMPERATURE,
        'stream': stream
    }

    try:
        resp = requests.post(
            f'{AIConfig.BASE_URL}/chat/completions',
            headers=headers, json=payload, timeout=AIConfig.TIMEOUT, stream=stream
        )
        if resp.status_code == 401:
            return {'success': False, 'error': 'API密钥无效'}
        if resp.status_code != 200:
            return {'success': False, 'error': f'AI服务异常({resp.status_code})'}

        if stream:
            return resp  # 流式模式返回原始response对象
        else:
            data = resp.json()
            return {'success': True, 'answer': data['choices'][0]['message']['content']}

    except requests.exceptions.Timeout:
        return {'success': False, 'error': '请求超时'}
    except Exception as e:
        return {'success': False, 'error': str(e)}


# ============================================================
#  路由
# ============================================================
"""
Flask 主应用
============
“江西水文化数字展馆”后端服务

启动方式：
    python app.py

访问地址：
    http://localhost:5000

包含路由：
    GET  /                           → 展馆主页
    POST /api/guide/ask              → 普通问答
    POST /api/guide/ask-stream       → 流式问答（SSE）
    GET  /api/guide/health           → 健康检查
"""
@app.route('/')
def index():
    return render_template('pavilion.html')


@app.route('/api/guide/ask', methods=['POST'])
def guide_ask():
    """普通问答"""
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'success': False, 'error': '请提供问题'}), 400
    result = call_llm(data['question'].strip(),
                      custom_prompt=data.get('custom_prompt'))
    return jsonify(result)



@app.route('/api/guide/ask-stream', methods=['POST'])
def guide_ask_stream():
    """流式问答（SSE）—— 教学难点"""
    data = request.get_json()
    if not data or 'question' not in data:
        return Response(f"data: {json.dumps({'error': '请提供问题'}, ensure_ascii=False)}\n\n",
                        mimetype='text/event-stream')

    resp = call_llm(data['question'].strip(), stream=True,
                    custom_prompt=data.get('custom_prompt'))
    # 没有提示词的回答
    # resp = call_llm(data['question'].strip(), stream=True,
    #                 custom_prompt=EMPTY_PROMPT)
    def generate():
        if isinstance(resp, dict):  # 错误
            yield f"data: {json.dumps(resp, ensure_ascii=False)}\n\n"
            return
        for line in resp.iter_lines():
            if not line: continue
            line_str = line.decode('utf-8')
            if not line_str.startswith('data: '): continue
            data_str = line_str[6:]
            if data_str.strip() == '[DONE]': break
            try:
                chunk = json.loads(data_str)
                content = chunk['choices'][0]['delta'].get('content', '')
                if content:
                    yield f"data: {json.dumps({'content': content}, ensure_ascii=False)}\n\n"
            except: continue
        yield f"data: {json.dumps({'done': True})}\n\n"

    return Response(generate(), mimetype='text/event-stream',
                    headers={'Cache-Control': 'no-cache', 'Connection': 'keep-alive'})


@app.route('/api/guide/health', methods=['GET'])
def health():
    """健康检查"""
    result = call_llm('你好，请用一句话介绍你自己')
    return jsonify({'status': 'ok' if result['success'] else 'error',
                    'message': result.get('answer', result.get('error', ''))[:80]})


@app.errorhandler(404)
def not_found(e):
    return jsonify({'success': False, 'error': '接口不存在'}), 404

# ============================================================
#  演示路由：无Prompt vs 有Prompt 对比
# ============================================================

# 一个“裸”的System Prompt —— 故意不设任何限制
EMPTY_PROMPT = "你是一个AI助手，请回答用户的问题。"
@app.route('/api/guide/compare', methods=['POST'])
def guide_compare():
    """
    对比演示接口
    同时返回“无Prompt”和“有Prompt”两种回答

    请求: POST /api/guide/compare
    Body: {"question": "请介绍鄱阳湖"}

    返回: {
        "question": "...",
        "without_prompt": "百科式通用回答...",
        "with_prompt": "水文化导游式回答..."
    }
    """
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'success': False, 'error': '请提供问题'}), 400

    question = data['question'].strip()

    # 左边：无Prompt（通用回答）
    result1 = call_llm(question, custom_prompt=EMPTY_PROMPT)

    # 右边：有Prompt（水文化导游）
    result2 = call_llm(question, custom_prompt=SYSTEM_PROMPT)

    return jsonify({
        'success': True,
        'question': question,
        'without_prompt': result1.get('answer', result1.get('error', '')),
        'with_prompt': result2.get('answer', result2.get('error', ''))
    })



if __name__ == '__main__':
    if AIConfig.API_KEY == 'your-api-key-here':
        print('⚠️  请先配置API_KEY: export DEEPSEEK_API_KEY=你的密钥')
    else:
        print('✅ 服务启动: http://localhost:5000')
    app.run(debug=True, host='0.0.0.0', port=5001)
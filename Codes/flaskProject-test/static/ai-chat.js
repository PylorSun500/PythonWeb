/**
 * 水文化智能导游 - 前端聊天组件
 * 核心功能：SSE流式对话、打字机效果、对话历史
 */
class WaterCultureChat {
    constructor() {
        this.messagesBox = document.getElementById('ai-chat-messages');
        this.inputField = document.getElementById('ai-chat-input');
        this.sendBtn = document.getElementById('ai-chat-send');
        this.isWaiting = false;

        this.sendBtn.addEventListener('click', () => this.send());
        this.inputField.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') { e.preventDefault(); this.send(); }
        });
        document.querySelectorAll('.quick-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                this.inputField.value = btn.dataset.question;
                this.send();
            });
        });

        this._addMsg('ai', '您好！我是小潦 🌊，江西水文化展馆的AI导游。\n请问想了解什么？');
    }

    async send() {
        const question = this.inputField.value.trim();
        if (!question || this.isWaiting) return;
        this.inputField.value = '';
        this._addMsg('user', question);
        this._setWaiting(true);

        const msgEl = this._addMsg('ai', '');
        let fullText = '';

        try {
            const resp = await fetch('/api/guide/ask-stream', {  //ai回答
            // const resp = await fetch('/api/guide/ask', {  //普通回答
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ question })
            });
            const reader = resp.body.getReader();
            const decoder = new TextDecoder();
            let buf = '';

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;
                buf += decoder.decode(value, { stream: true });
                const lines = buf.split('\n');
                buf = lines.pop() || '';

                for (const line of lines) {
                    if (!line.startsWith('data: ')) continue;
                    try {
                        const data = JSON.parse(line.slice(6));
                        if (data.error) { msgEl.textContent = '❌ ' + data.error; msgEl.className = 'message error'; return; }
                        if (data.done) return;
                        if (data.content) { fullText += data.content; msgEl.textContent = fullText; }
                    } catch (e) {}
                }
            }
        } catch (e) {
            msgEl.textContent = '❌ 网络错误，请稍后重试';
            msgEl.className = 'message error';
        } finally {
            this._setWaiting(false);
            this.inputField.focus();
        }
    }

    _addMsg(type, text) {
        const div = document.createElement('div');
        div.className = `message ${type}`;
        div.textContent = text;
        this.messagesBox.appendChild(div);
        this.messagesBox.scrollTop = this.messagesBox.scrollHeight;
        return div;
    }

    _setWaiting(waiting) {
        this.isWaiting = waiting;
        this.sendBtn.disabled = waiting;
        this.inputField.disabled = waiting;
    }
}

document.addEventListener('DOMContentLoaded', () => new WaterCultureChat());
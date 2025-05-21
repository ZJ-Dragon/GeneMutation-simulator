# GeneMutation-simulator

> 一款前后端结合的基因突变模拟工具  
> 前端使用 Material Web（MD3）组件，后端基于 Flask + Biopython，支持替换、插入、缺失三种突变类型，实时显示编码链、mRNA 序列和中文氨基酸翻译。

---

## 🌟 功能亮点

- **直观可视化**  
  - DNA 模板链 (3′→5′)、编码链 (5′→3′)、mRNA (5′→3′) 串联展示  
  - 中文氨基酸名称原位翻译  
- **三种突变模拟**  
  - `替换`（substitution）  
  - `插入`（insertion）  
  - `缺失`（deletion）  
- **前端交互**  
  - Material Design 风格的圆角 pill 按钮  
  - 当选中“缺失”时自动隐藏碱基输入  
  - 输入框与按钮悬停、选中状态均有动画反馈  
- **后端封装**  
  - Flask 提供 `/mutate` JSON API  
  - Biopython 负责互补链、转录、翻译，保证生物信息学计算正确性  
- **历史记录**  
  - 每次操作都会在页面底部追加日志，支持对比“前 → 后”序列  

---

## 📦 安装与运行

### 1. 克隆仓库

```bash
git clone https://github.com/yourname/GeneMutation-simulator.git
cd GeneMutation-simulator
```

2. 创建并激活虚拟环境

```bash
python -m venv venv
```

3. 安装依赖

```bash
pip install -r requirements.txt
```


4. 启动服务

```bash
python app.py
```

服务器启动后，会在控制台输出：

```* Running on http://127.0.0.1:7777```

5. 打开浏览器

访问 http://127.0.0.1:7777，即可看到基因突变模拟器界面。

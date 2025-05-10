window.mdc.autoInit();

async function mutateRequest(payload){
    const res = await fetch('/mutate', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(payload)
    });
    return await res.json();     // 解析响应  [oai_citation:14‡MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Response/json?utm_source=chatgpt.com)
}

runBtn.onclick = async ()=>{
    const payload = { template: templateDNA, type, pos, base };
    const data = await mutateRequest(payload);

    // 使用 data.template / data.coding / data.mrna / data.amino
    // 调用原来的 colour() 和 renderAll() 重绘
};
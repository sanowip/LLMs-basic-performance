
import zhipuai
def zhipu(s1,s2):
    zhipuai.api_key = "4475a18b319bdb34de446d8682d36820.RxM0Wq87aJUwZyL9"
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=[
            {"role": "user", "content": s1},
        ],
        temperature=0.95,
        top_p=0.7,
        incremental=True
    )
    res=""
    for event in response.events():
        if event.event == "add":
            res+=event.data
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
        elif event.event == "finish":
            print(event.data)
            print(event.meta)
        else:
            print(event.data)
    res2=""
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=[
            {"role": "user", "content": s1},
            {"role": "assistant", "content": res},
            {"role": "user", "content": s2},
        ],
        temperature=0.95,
        top_p=0.7,
        incremental=True
    )
    for event in response.events():
        if event.event == "add":
            res2+=event.data
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
        elif event.event == "finish":
            print(event.data)
            print(event.meta)
        else:
            print(event.data)
    return [res,res2]

### **Базовый пример реализации**
Устанавливаем библиотеку
````bash
pip install integra-python-connector
````

Создаем новый процессор:
````python
import json
from pathlib import Path

from integra_python_connect.adapters import ProcessorAdapter
from integra_python_connect.dto import SkeletonProcessor, ProcessorView
from integra_python_connect import Bridge


class ExampleProcessor(ProcessorAdapter):
    async def execute(self, exchange: str = None):
        body = json.loads(exchange["body"]["stringBody"])
        body['test'] = 'value'
        new_body = json.dumps(body)
        exchange["body"]["stringBody"] = new_body
        return exchange

    async def get_view(self) -> ProcessorView:
        skeleton = SkeletonProcessor(type_processor='Example type')
        return ProcessorView(
            processor_title="Example",
            processor_description="Example description",
            skeleton_processor=skeleton
        )
    
    async def validate(self, exchange: str = None):
        return "VALIDATED!"

````
Инициализируем сам сервис:
````python
bridge = Bridge(
    title='Example service',
    address='Example address',
    description='Example description',
    manual_path=Path(__file__).parent / 'manual.pdf'
)
bridge.register_handlers([ExampleProcessor, ])
application = bridge.build()
````

Запускаем web-сервер:
````python
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="__main__:application", host='localhost', port=8002)

````
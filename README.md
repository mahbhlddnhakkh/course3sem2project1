## Open3D python
### Создать venv
```sh
python -m venv venv
```
### Перейти в venv:
#### Linux:
```sh
source venv/bin/activate
```
#### Windows:
```sh
venv\Scripts\activate.bat
```
### Установить модули (в venv):
```sh
pip install -r requirements.txt
```
### Запуск (в venv):
```sh
python mesh-test1.py [-h] [--models [{ArmadilloMesh,KnotMesh,AvocadoModel,DamagedHelmetModel,FlightHelmetModel,MonkeyModel,SwordModel} ...]] [--draw [{vis_spin,o3dvis_spin,draw_geometries,draw,draw_geometries_wireframe,draw_geometries_back_face,draw_geometries_wireframe_back_face} ...]]
```
## Renderdoc
### Установить renderdoc
https://renderdoc.org/
### Как загружать захваченные кадры renderdoc
File -> Open Capture\
Или CTRL+O
### Как открыть счётчик производительности
https://renderdoc.org/docs/window/performance_counter_viewer.html
### Мои захваты:
- `mesh-test1.py --models KnotMesh KnotMesh --draw o3dvis_spin`\
Рендерит 2 простых [TriangleMesh](https://www.open3d.org/docs/release/python_api/open3d.geometry.TriangleMesh.html) [KnotMesh](https://www.open3d.org/docs/release/python_api/open3d.data.KnotMesh.html), используя [O3DVisualizer](https://www.open3d.org/docs/release/python_api/open3d.visualization.O3DVisualizer.html) с анимацией.\
Файл renderdoc: `mesh-test1_KnotMesh_KnotMesh_o3dvis_spin.rdc`\
Счётчик производительности: `mesh-test1_KnotMesh_KnotMesh_o3dvis_spin.csv`
- `mesh-test1.py --models KnotMesh KnotMesh --draw o3dvis_spin`\
Рендерит 2 простых [TriangleMesh](https://www.open3d.org/docs/release/python_api/open3d.geometry.TriangleMesh.html) [KnotMesh](https://www.open3d.org/docs/release/python_api/open3d.data.KnotMesh.html), используя [Visualizer](https://www.open3d.org/docs/release/python_api/open3d.visualization.Visualizer.html) с анимацией.\
Файл renderdoc: `mesh-test1_KnotMesh_KnotMesh_vis_spin.rdc`\
Счётчик производительности: `mesh-test1_KnotMesh_KnotMesh_vis_spin.csv`
### Как захватывать
Перейти в `Launch Application`, нажать на `Load Settings` и загрузить `settings_example_linux.cap` или `settings_example_windows.cap`. Далее в `Executable path` и в `Working Directory` необходимо заменить `<path-to-project-dir>` на путь к папке с проектом. В `Command-line Arguments` идёт [запуск с параметрами, которые можно менять](#запуск-в-venv). Можно также сохранить конфигурацию с исправленными путями, нажав на `Load Settings`. Далее необходимо нажать на `launch`.\
Для захвата кадра (так получается лучше всего): выбрать задержку `1 secs` или больше и нажать на `Capture After Delay`. В течение этого времени необходимо сделать окно Open3D активным и, если отсутствует анимация, делать любые действия камерой, чтобы объекты в кадре постоянно перерисовывались, иначе их прорисовка не захватывается, что очевидно (зачем перерисовывать статический кадр постоянно?).
## Проблемы
- `--draw o3dvis_spin` с любыми `Model` (которые с текстурами, например, `AvocadoModel`) будет крайне сильно тормозить. С такими моделями для тестирования [O3DVisualizer](https://www.open3d.org/docs/release/python_api/open3d.visualization.Visualizer.html) необходимо использовать `--draw draw`, а для захвата - вручную "дёргать" камеру.
- Модель [BunnyMesh](https://www.open3d.org/docs/release/python_api/open3d.data.BunnyMesh.html) по какой-то причине странно себя ведёт, когда используется вместе с другими моделями. Эта модель и следующая после неё просто не отображается. Но уже третья отображается нормально. Поэтому я просто исключил её из списка моделей.

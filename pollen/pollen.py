from flask import Blueprint, render_template
from api.api import PollenAPI

pollen_bp = Blueprint(name='pollen_bp', import_name=__name__,
                      template_folder='templates', static_folder='static',
                      static_url_path='assets')


@pollen_bp.route('/')
def graph():
    pollen_api = PollenAPI()
    data = pollen_api.call_api(location="38.581573, -121.494400",
                               pollen_list=["treeBirchIndex", "treeAshIndex", "treeOakIndex", "treeElmIndex"])
    pollen_fields = ['Pollen Type'] + pollen_api.get_fields()
    pollen_data = [pollen_fields] + data
    # test_data = [['Pollen Type', 'treeBirchIndex', 'treeAshIndex', 'treeOakIndex', 'treeIndex'],
    #              ['2023-07-07', 3, 2, 1, 1], ['2023-07-08', 1, 3, 1, 4], ['2023-07-09', 2, 4, 1, 3],
    #              ['2023-07-10', 2, 0, 3, 1], ['2023-07-11', 2, 0, 0, 0], ['2023-07-12', 3, 2, 3, 0]]
    return render_template('pollen/graph.html', pollen_data=pollen_data)

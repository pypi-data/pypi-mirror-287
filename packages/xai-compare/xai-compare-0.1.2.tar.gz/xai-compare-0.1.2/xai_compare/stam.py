import pandas as pd

from xai_compare.config import MODE
from xai_compare.abstract.explainer import Explainer

# load data
X_train = ""
y_train = ""
# train model
model = ""
# declare the task type
mode = MODE.REGRESSION

class CustomExplainer(Explainer):

    def explain_global(self, x_data: pd.DataFrame) -> pd.DataFrame:
        pass

    def explain_local(self, x_data: pd.DataFrame) -> pd.DataFrame:
        pass


custom_explainer = CustomExplainer(
    model,
    X_train,
    y_train,
    mode
)

# create exapiner_factory

# create comparison factory
comparison_factory_obj = ""
# run the analysis
analysis_results = comparison_factory_obj.run()

# report
analysis_results.plot_diagnostic()


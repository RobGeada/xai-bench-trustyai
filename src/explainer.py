from xai_bench_trustyai import custom_explainers

valid_explainers = {
    "shap_trustyai": custom_explainers.shap.KernelShapTrustyAI,
    "shap": custom_explainers.KernelShap,
    "random": custom_explainers.Random,
    "lime": custom_explainers.Lime,
    "lime_trustyai": custom_explainers.LimeTrustyAI,
}


class Explainer:
    def __init__(self, name, **kwargs):
        if name not in valid_explainers.keys():
            raise NotImplementedError(
                f"This explainer ({name}) is not supported at the moment. Explainers supported are {list(valid_explainers.keys())}"
            )
        self.name = name
        def explainerinit(clf, data, modelname):
            kwargs['model_name'] = modelname
            return valid_explainers[name](clf, data, **kwargs)

        self.explainer = explainerinit
        self.label = kwargs.get("label", "default")

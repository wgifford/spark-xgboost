#
# Copyright (c) 2019 by Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from pyspark import keyword_only

from sparkxgb.common import XGboostEstimator, XGboostModel


class XGBoostClassifier(XGboostEstimator):
    """
    A PySpark wrapper of ml.dmlc.xgboost4j.scala.spark.XGBoostClassifier
    """

    @keyword_only
    def __init__(
        self,
        alpha=0.0,
        baseMarginCol=None,
        baseScore=0.5,
        cacheTrainingSet=False,
        checkpointInterval=-1,
        checkpointPath="",
        colsampleBylevel=1.0,
        colsampleBytree=1.0,
        contribPredictionCol=None,
        ## EXCLUDED: customEval=None,
        ## EXCLUDED: customObj=None,
        eta=0.3,
        evalMetric=None,
        featuresCol="features",
        gamma=0.0,
        growPolicy="depthwise",
        interactionConstraints=None,
        labelCol="label",
        lambda_=1.0,  # Rename of 'lambda' param, as this is a reserved keyword in python.
        lambdaBias=0.0,
        leafPredictionCol=None,
        maxBins=16,
        maxDeltaStep=0.0,
        maxDepth=6,
        maxLeaves=None,
        maximizeEvaluationMetrics=None,
        minChildWeight=1.0,
        missing=float("nan"),
        monotoneConstraints=None,
        normalizeType="tree",
        nthread=1,
        numClass=None,
        numEarlyStoppingRounds=0,
        numRound=1,
        numWorkers=1,
        objective="reg:squarederror",
        objectiveType=None,
        predictionCol="prediction",
        probabilityCol="probability",
        rateDrop=0.0,
        rawPredictionCol="rawPrediction",
        sampleType="uniform",
        scalePosWeight=1.0,
        seed=0,
        silent=0,
        sketchEps=0.03,
        skipDrop=0.0,
        subsample=1.0,
        thresholds=None,
        timeoutRequestWorkers=1800000,
        ## EXCLUDED: trackerConf=None,
        trainTestRatio=1.0,
        treeLimit=0,
        treeMethod="auto",
        useExternalMemory=False,
        verbosity=1,
        weightCol=None,
    ):
        super(XGBoostClassifier, self).__init__(
            classname="ml.dmlc.xgboost4j.scala.spark.XGBoostClassifier"
        )
        kwargs = self._input_kwargs
        if "lambda_" in kwargs:
            kwargs["lambda"] = kwargs.pop("lambda_")
        self.setParams(**kwargs)

    @keyword_only
    def setParams(
        self,
        alpha=0.0,
        baseMarginCol=None,
        baseScore=0.5,
        cacheTrainingSet=False,
        checkpointInterval=-1,
        checkpointPath="",
        colsampleBylevel=1.0,
        colsampleBytree=1.0,
        contribPredictionCol=None,
        ## EXCLUDED: customEval=None,
        ## EXCLUDED: customObj=None,
        eta=0.3,
        evalMetric=None,
        featuresCol="features",
        gamma=0.0,
        growPolicy="depthwise",
        interactionConstraints=None,
        labelCol="label",
        lambda_=1.0,  # Rename of 'lambda' param, as this is a reserved keyword in python.
        lambdaBias=0.0,
        leafPredictionCol=None,
        maxBins=16,
        maxDeltaStep=0.0,
        maxDepth=6,
        maxLeaves=None,
        maximizeEvaluationMetrics=None,
        minChildWeight=1.0,
        missing=float("nan"),
        monotoneConstraints=None,
        normalizeType="tree",
        nthread=1,
        numClass=None,
        numEarlyStoppingRounds=0,
        numRound=1,
        numWorkers=1,
        objective="reg:squarederror",
        objectiveType=None,
        predictionCol="prediction",
        probabilityCol="probability",
        rateDrop=0.0,
        rawPredictionCol="rawPrediction",
        sampleType="uniform",
        scalePosWeight=1.0,
        seed=0,
        silent=0,
        sketchEps=0.03,
        skipDrop=0.0,
        subsample=1.0,
        thresholds=None,
        timeoutRequestWorkers=1800000,
        ## EXCLUDED: trackerConf=None,
        trainTestRatio=1.0,
        treeLimit=0,
        treeMethod="auto",
        useExternalMemory=False,
        verbosity=1,
        weightCol=None,
    ):
        kwargs = self._input_kwargs
        return self._set(**kwargs)

    def _create_model(self, java_model):
        return XGBoostClassificationModel(java_model=java_model)


class XGBoostClassificationModel(XGboostModel):
    """
    A PySpark wrapper of ml.dmlc.xgboost4j.scala.spark.XGBoostClassificationModel
    """

    def __init__(
        self,
        classname="ml.dmlc.xgboost4j.scala.spark.XGBoostClassificationModel",
        java_model=None,
    ):
        super(XGBoostClassificationModel, self).__init__(
            classname=classname, java_model=java_model
        )

    @property
    def nativeBooster(self):
        """
        Get the native booster instance of this model.
        This is used to call low-level APIs on native booster, such as "getFeatureScore".
        """
        return self._call_java("nativeBooster")


class XGBoostRegressor(XGboostEstimator):
    """
    A PySpark wrapper of ml.dmlc.xgboost4j.scala.spark.XGBoostRegressor
    """

    @keyword_only
    def __init__(
        self,
        allowNonZeroForMissing=False,
        alpha=0.0,
        baseMarginCol=None,
        baseScore=0.5,
        cacheTrainingSet=False,
        checkpointInterval=-1,
        checkpointPath="",
        colsampleBylevel=1.0,
        colsampleBytree=1.0,
        contribPredictionCol=None,
        ## EXCLUDED: customEval=None,
        ## EXCLUDED: customObj=None,
        eta=0.3,
        evalMetric=None,
        gamma=0.0,
        groupCol=None,
        growPolicy="depthwise",
        interactionConstraints=None,
        lambda_=1.0,  # Rename of 'lambda' param, as this is a reserved keyword in python.
        lambdaBias=0.0,
        leafPredictionCol=None,
        maxBin=256,
        maxDeltaStep=0.0,
        maxDepth=6,
        maxLeaves=None,
        maximizeEvaluationMetrics=None,
        minChildWeight=1.0,
        missing=float("nan"),
        monotoneConstraints=None,
        normalizeType="tree",
        nthread=1,
        numClass=None,
        numEarlyStoppingRounds=0,
        numRound=1,
        numWorkers=1,
        objective="reg:squarederror",
        objectiveType=None,
        probabilityCol="probability",
        rateDrop=0.0,
        rawPredictionCol="rawPrediction",
        sampleType="uniform",
        scalePosWeight=1.0,
        seed=0,
        silent=0,
        sketchEps=0.03,
        skipDrop=0.0,
        subsample=1.0,
        timeoutRequestWorkers=1800000,
        ## EXCLUDED: trackerConf=None,
        trainTestRatio=1.0,
        treeLimit=0,
        treeMethod="auto",
        useExternalMemory=False,
        verbosity=1,
        weightCol=None,
    ):
        super(XGBoostRegressor, self).__init__(
            classname="ml.dmlc.xgboost4j.scala.spark.XGBoostRegressor"
        )
        kwargs = self._input_kwargs
        # if "lambda_" in kwargs:
        #     kwargs["lambda"] = kwargs.pop("lambda_")

        self._setDefault(
            allowNonZeroForMissing=False,
            alpha=0.0,
            baseScore=0.5,
            cacheTrainingSet=False,
            checkpointInterval=-1,
            checkpointPath="",
            colsampleBylevel=1.0,
            colsampleBytree=1.0,
            dmlcWorkerConnectRetry=5,
            eta=0.3,
            featuresCol="features",
            gamma=0.0,
            growPolicy="depthwise",
            killSparkContextOnWorkerFailure=True,
            labelCol="label",
            lambdaBias=0.0,
            maxBin=256,
            maxDeltaStep=0.0,
            maxDepth=6,
            minChildWeight=1.0,
            missing=float("nan"),
            normalizeType="tree",
            nthread=1,
            numEarlyStoppingRounds=0,
            numRound=1,
            numWorkers=1,
            objective="reg:squarederror",
            predictionCol="prediction",
            rabitRingReduceThreshold=32768,
            rabitTimeout=-1,
            rateDrop=0.0,
            sampleType="uniform",
            scalePosWeight=1.0,
            seed=0,
            silent=0,
            sketchEps=0.03,
            skipDrop=0.0,
            subsample=1.0,
            timeoutRequestWorkers=1800000,
            trainTestRatio=1.0,
            treeLimit=0,
            treeMethod="auto",
            useExternalMemory=False,
            verbosity=1,
        )
        # handle default for lambda
        self._setDefault(**{"lambda": 1.0})
        self.setParams(**kwargs)

    @keyword_only
    def setParams(
        self,
        allowNonZeroForMissing=False,
        alpha=0.0,
        baseMarginCol=None,
        baseScore=0.5,
        cacheTrainingSet=False,
        checkpointInterval=-1,
        checkpointPath="",
        colsampleBylevel=1.0,
        colsampleBytree=1.0,
        contribPredictionCol=None,
        ## EXCLUDED: customEval=None,
        ## EXCLUDED: customObj=None,
        eta=0.3,
        evalMetric=None,
        gamma=0.0,
        groupCol=None,
        growPolicy="depthwise",
        interactionConstraints=None,
        lambda_=1.0,  # Rename of 'lambda' param, as this is a reserved keyword in python.
        lambdaBias=0.0,
        leafPredictionCol=None,
        maxBin=256,
        maxDeltaStep=0.0,
        maxDepth=6,
        maxLeaves=None,
        maximizeEvaluationMetrics=None,
        minChildWeight=1.0,
        missing=float("nan"),
        monotoneConstraints=None,
        normalizeType="tree",
        nthread=1,
        numClass=None,
        numEarlyStoppingRounds=0,
        numRound=1,
        numWorkers=1,
        objective="reg:squarederror",
        objectiveType=None,
        probabilityCol="probability",
        rateDrop=0.0,
        rawPredictionCol="rawPrediction",
        sampleType="uniform",
        scalePosWeight=1.0,
        seed=0,
        silent=0,
        sketchEps=0.03,
        skipDrop=0.0,
        subsample=1.0,
        timeoutRequestWorkers=1800000,
        ## EXCLUDED: trackerConf=None,
        trainTestRatio=1.0,
        treeLimit=0,
        treeMethod="auto",
        useExternalMemory=False,
        verbosity=1,
        weightCol=None,
    ):
        kwargs = self._input_kwargs
        if "lambda_" in kwargs:
            kwargs["lambda"] = kwargs.pop("lambda_")
        return self._set(**kwargs)

    def _create_model(self, java_model):
        return XGBoostRegressionModel(java_model=java_model)


class XGBoostRegressionModel(XGboostModel):
    """
    A PySpark wrapper of ml.dmlc.xgboost4j.scala.spark.XGBoostRegressionModel
    """

    def __init__(
        self,
        classname="ml.dmlc.xgboost4j.scala.spark.XGBoostRegressionModel",
        java_model=None,
    ):
        super(XGBoostRegressionModel, self).__init__(
            classname=classname, java_model=java_model
        )

    @property
    def nativeBooster(self):
        """
        Get the native booster instance of this model.
        This is used to call low-level APIs on native booster, such as "getFeatureScore".
        """
        return self._call_java("nativeBooster")

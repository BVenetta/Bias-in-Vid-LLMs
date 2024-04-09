# A Deep Dive into Bias, Temporality, and Understanding in Video-Language Models

## Project description:
Large Language Models (LLMs) have demonstrated significant advancements, showcasing impressive generalization abilities across various tasks. The integration of LLMs with vision has led to the emergence of Vision-Language Models (VLMs), which excel in interpreting and generating visual and textual content. Extending these models into the video domain introduced complexities due to the added temporal dimension, increasing the data volume significantly. Video-Language Models changed the video understanding landscape, enabling responses to open-ended and multiple-choice questions beyond the conventional strict classification methods. Nevertheless, the shift towards such evaluation methods obscured the clarity of the models' true video understanding capabilities as we humans tend to be easily fooled by the chatty and fluent responses of VLMs. Consequently, this project is dedicated to an in-depth examination of autoregressive Video-Language Models, focusing on their video understanding abilities through probing several critical areas such as:

* Exploring the degree of bias inherited from LLMs and the reliance of model responses on memorized pre-existing knowledge, like movie narratives, as opposed to visual information.
* Assess the models' actual temporal understanding, including their reliance on visual cues or keyframes, and the hallucination of details. What happens if frames are omitted, blacked out or the temporal or visual content been changed?
* Evaluate the adequacy of existing benchmarks in measuring the capabilities of Video-Language Models. Can they be solved by the context of the question or with a single frame alone?
* Explore how various video-language training strategies influence the models' biases and effectiveness. Are instruction finetuned Video-Language Models superior for temporal understanding than pretrained models? [1] provides a great survey on existing Video-Language Models.

Based on these insights, the project can be extended to propose new pretraining designs or benchmarks for improved assessment of temporal understanding in video-language models.

References:
[1] Video Understanding with Large Language Models: A Survey. Yunlong Tang et al. [Arxiv.](https://arxiv.org/abs/2312.17432)

import fiftyone as fo
import fiftyone.zoo as foz

# Path to missing files
source_dir = "./videos"

# Download and load 10 samples from the validation split of ActivityNet 200
dataset = foz.load_zoo_dataset(
    "activitynet-200",
    split="validation",
    max_samples=3,
)

if __name__ == "__main__":
    # Ensures that the App processes are safely launched on Windows
    session = fo.launch_app(dataset)
    session.wait()
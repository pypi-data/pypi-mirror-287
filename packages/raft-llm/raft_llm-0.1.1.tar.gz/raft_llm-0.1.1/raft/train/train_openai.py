import json
from openai import OpenAI
import sys
import os
import time
from typing import List, Dict, Any, Literal, Optional

def train(
    dataset_path: str,
    model_name: str = "gpt-4o-mini"
    ) -> Dict[str, Any]:
    assert(os.path.isfile(dataset_path))
    assert("jsonl" in dataset_path)
    client = OpenAI()
    # Upload the dataset
    response = client.files.create(
        file=open(dataset_path, "rb"),
        purpose="fine-tune"
    )
    dataset_id = response.id
    print(f"Dataset uploaded with ID: {dataset_id}")

    # Fine-tune the model
    fine_tune_response = client.fine_tuning.jobs.create(
        training_file=dataset_id,
        model=model_name  # You can change this to the model you prefer
    )

    print("Fine-tuning started:")
    fine_tune_job_id = fine_tune_response.id
    time_elapsed = 0
    while True:
        status_response = client.fine_tuning.jobs.retrieve(fine_tune_job_id)
        status = status_response.status
        status_message = f"\rFine-tuning status: {status}".ljust(previous_status_message_length)
        previous_status_message_length = len(status_message)
        sys.stdout.write(status_message)
        sys.stdout.flush()
        if status == 'succeeded':
            model_name = status_response.fine_tuned_model
            print(f"\nFine-tuning succeeded. Model name: {model_name}")
            print(f"Fine-tuning took {time_elapsed} seconds.")
            return {"model_name": model_name}
        elif status == 'failed':
            print("Fine-tuning failed.")
            return {"error": "Fine-tuning failed."}
        elif time_elapsed > 3600:
            print("Fine-tuning took too long.")
            return {"error": "Fine-tuning took too long."}
        
        time.sleep(10)
        time_elapsed += 10

if __name__ == "__main__":
    dataset_path = "train_openai.jsonl"
    if not os.path.isfile(dataset_path):
        print(f"File {dataset_path} does not exist. Please provide a valid dataset file.")
    else:
        response = train(dataset_path)
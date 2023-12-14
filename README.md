# Image retrieval with Azure Computer Vision V4.0 using vector embeddings

Multi-modal embedding involves converting images into numerical vectors to encapsulate their features and traits. These vectors encode an image's content and context in a manner that facilitates text-based search within the same vector space. While traditional image retrieval relied on extracted features like labels and descriptors, the rising preference for vector similarity search stems from its advantages over keyword-based methods. contemporary content search services.

![image](https://github.com/glauberss2007/AI-Image-Retrieval-Matching/assets/22028539/2e151efd-f2da-44d0-9a75-0f1bd3e50057)

Vector embeddings serve as a method to portray content, be it text or images, in the form of numerical vectors within a multi-dimensional space. Typically derived from extensive textual and visual datasets through machine learning techniques like neural networks, these embeddings map each vector dimension to distinct content features or characteristics. These attributes encompass semantic significance, syntactic function, or the prevalent context in which the content is observed.

## Vectorization Process

### Image Vectorization (VectorizeImage)

- Extract feature vectors from images using the `VectorizeImage` API.
- Generate a single feature vector representing the entire image content.

### Text Vectorization (VectorizeText)

- Utilize the `VectorizeText` API to extract feature vectors from text inputs.
- Generate a feature vector that encapsulates the semantic and contextual attributes of the text.

## Similarity Measurement

### Distance Metrics

- Vector search systems employ metrics like cosine or Euclidean distance to measure similarity.
- In the Vision studio demo, cosine distance is utilized for similarity assessment.

## Image Retrieval

### Fetching Similar Images

- Identify top N similar vectors to the search query.
- Retrieve corresponding images from your photo library based on these vectors.
- Present these images as the final output.

## Applications of Multi-Modal Embedding

Multi-modal embedding has a variety of applications in different fields, including:

- **Digital Asset Management:** Multi-modal embedding is integral in organizing extensive collections of digital images, prevalent in museums, archives, or online galleries. This functionality enables users to search for images based on their visual attributes, enhancing retrieval based on specific criteria.
- **Security and Surveillance:** In security and surveillance systems, vectorization plays a crucial role. It enables image searches grounded in distinct features or patterns, offering support in tasks like people & object tracking and threat detection.
- **Forensic Image Retrieval:** Vectorization serves a pivotal role in forensic investigations, facilitating image searches based on visual content or metadata. Particularly essential in cases involving cyber-crime, this capability aids in comprehensive investigative procedures.
- **E-commerce Enhancement:** Within online shopping applications, vectorization enhances the user experience. It allows for searching similar products based on their distinguishing features or descriptions. Additionally, it powers recommendation systems derived from previous purchase patterns.
- **Fashion and Design Innovations:** In the realm of fashion and design, vectorization empowers image searches based on visual elements like color, pattern, or texture. This functionality aids designers and retailers in identifying similar products or recognizing emerging trends.

## Code example

The python code in this repository ([exmaples.py](https://github.com/glauberss2007/AI-Image-Retrieval-Matching/blob/main/examples.py)) is designed to leverage Azure Cognitive Services for image and text embeddings, utilizing the Azure CV 4.0 capabilities. It begins by defining endpoint URLs and necessary headers for API requests. The functions image_embedding() and text_embedding() handle the embedding process for images and text, respectively. The cosine similarity between vectors is computed via get_cosine_similarity(). The similarity_results() function compares an image embedding with multiple text prompts, sorting and presenting the similarity scores in a Pandas DataFrame. The code then demonstrates this functionality by embedding several images, displaying them, and evaluating their similarity with predefined text prompts. Finally, cosine similarity calculations are performed between different image embeddings. The visualization of results uses libraries like Matplotlib, Seaborn, and Pandas to present the similarity scores in a more understandable format through color gradients in DataFrames.

## Automaticaly azure endpoint deployment using terraform

This [Terraform script](https://github.com/glauberss2007/AI-Image-Retrieval-Matching/blob/main/az-computer-vision.tf) sets up an Azure Cognitive Services account for Computer Vision, enables a system-assigned managed identity, and then creates an endpoint within that account. Remember to replace placeholders like your-cognitive-account-name, your-resource-group, your-location, your-sku, and others with your actual Azure-specific values and customize as needed for your infrastructure setup. If necessary, see below terraform instalation/configuration.

### Prerequisites

1. **Install Terraform:**
   - Download and install Terraform from [Terraform's official website](https://www.terraform.io/downloads.html).

2. **Azure CLI:**
   - Ensure you have Azure CLI installed and configured on your local machine.

3. **Azure Subscription:**
   - You need an active Azure subscription with the required permissions to create resources.

### Deployment Steps

1. **Create Directory:**
   - Create a new directory on your local machine.
   - Place the Terraform configuration file in this directory. Name the file with a `.tf` extension (e.g., `main.tf`).

2. **Initialize Terraform:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing your Terraform file (`cd /path/to/directory`).
   - Run `terraform init` to initialize Terraform in that directory.

3. **Authenticate Azure CLI:**
   - Run `az login` in the terminal to log in to Azure via Azure CLI.
   - Follow the authentication steps prompted in your terminal.

4. **Set Azure Credentials:**
   - Set your Azure credentials using the following Azure CLI command:
     ```bash
     az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/{subscription-id}"
     ```
     This command will output the necessary credentials (`client_id`, `client_secret`, `tenant_id`, `subscription_id`). Keep these for the next step.

5. **Set Terraform Environment Variables:**
   - Set environment variables for Azure credentials using the values obtained in the previous step:
     ```bash
     export ARM_CLIENT_ID="your_client_id"
     export ARM_CLIENT_SECRET="your_client_secret"
     export ARM_SUBSCRIPTION_ID="your_subscription_id"
     export ARM_TENANT_ID="your_tenant_id"
     ```

6. **Deploy Terraform Configuration:**
   - Run `terraform plan` to preview changes that Terraform will make.
   - Run `terraform apply` to create the Azure Cognitive Services account based on the defined configuration.

7. **Confirm Deployment:**
   - Review the output in the terminal to ensure the deployment was successful.
   - Check your Azure portal to verify the creation of the Cognitive Services account.

Remember to replace placeholders like `your-cognitive-account-name`, `your-resource-group`, `your-location`, `your-sku`, and others with your actual Azure-specific values in the Terraform configuration file.

PS: Always exercise caution when deploying resources, especially in a production environment, and ensure you understand the implications of the changes being made.

# References

https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval
https://github.com/retkowsky
https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-image-retrieval#business-applications









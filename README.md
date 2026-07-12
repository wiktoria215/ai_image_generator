# AI Image Generator via Hugging Face API 🎨☁️

A lightweight Python script that generates high-quality images from text descriptions using the **FLUX.1** model hosted on the Hugging Face cloud infrastructure. 

This project demonstrates how to successfully integrate with a third-party Cloud API, manage authentication, and handle network requests using Python.

## 🚀 Features
* **Text-to-Image Generation:** Uses the state-of-the-art FLUX.1-schnell model to create detailed images.
* **API Integration:** Connects to the Hugging Face Serverless Inference API.
* **Error Handling:** Built-in checks for HTTP status codes to diagnose network, authentication, or provider-side issues.
* **Secure:** Uses environment variables/placeholders for API tokens to prevent credential leaks.

## 🛠️ Technologies
* **Language:** Python 3
* **Libraries:** `requests`
* **Cloud/AI:** Hugging Face API, FLUX.1 by Black Forest Labs

## ⚙️ How to Run Locally

1. Clone this repository to your local machine.
2. Make sure you have the `requests` library installed:
   ```bash
   pip install requests

## Troubleshooting & Cloud Networking
  During the development of this tool, I encountered and resolved several typical cloud-infrastructure challenges:

    % HTTP 410 (Gone): Handled model deprecation when the provider removed the older Stable Diffusion model from the free API tier.

    % HTTP 400 (Bad Request): Diagnosed unsupported model routing.

    % DNS Resolution Errors (Errno 11001): Identified and bypassed local firewall/DNS blocks by switching network routing, and experienced vendor-side DNS outages, which led to upgrading the endpoint to a more stable router gateway.

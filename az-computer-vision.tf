# Provider block specifies the Azure provider
provider "azurerm" {
  features {} # Optional features can be specified here
}

# Resource block for creating an Azure Cognitive Services account
resource "azurerm_cognitive_account" "example" {
  name                = "your-cognitive-account-name" # Name for the Cognitive Services account
  resource_group_name = "your-resource-group" # Name of the Azure resource group where the account will be created
  location            = "your-location" # Azure region where the resources will be deployed
  sku                 = "your-sku"  # SKU or tier for the Cognitive Services account (e.g., "F0" for free tier, "S0" for standard tier)
  kind                = "ComputerVision"  # Type of Cognitive Service, in this case, Computer Vision

  # Setting up system-assigned managed identity for the Cognitive Services account
  identity {
    type = "SystemAssigned"
  }
}

# Resource block for creating an endpoint within the Cognitive Services account
resource "azurerm_cognitive_account_endpoint" "example_endpoint" {
  name                = "your-endpoint-name" # Name for the endpoint
  resource_group_name = azurerm_cognitive_account.example.resource_group_name # Reference to the resource group name from the created Cognitive Services account
  account_name        = azurerm_cognitive_account.example.name # Reference to the Cognitive Services account name
  location            = azurerm_cognitive_account.example.location # Reference to the location of the Cognitive Services account
  sku                 = azurerm_cognitive_account.example.sku # Reference to the SKU/tier of the Cognitive Services account
  kind                = azurerm_cognitive_account.example.kind # Reference to the kind/type of Cognitive Service
  cognitive_services_account_id = azurerm_cognitive_account.example.id # Reference to the ID of the Cognitive Services account
}

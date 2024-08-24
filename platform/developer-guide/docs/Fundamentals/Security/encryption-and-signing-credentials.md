
To protect the tokens it issues, Virto Commerce uses the **encryption credentials to ensure the content of tokens cannot read by malicious parties**. They can be either asymmetric (e.g, an RSA key) or symmetric.

## Use self-signed certificate

Self-signed certificate is generated and stored in the database at the first platform startup.
  
To regenerate the certificate:

1. Stop all the platform instances.
1. Clear the `ServerCertificate` table in the database.
1. Run the platform again.

## Register certificate (recommended for production-ready scenarios)

To register a custom certificate, do the following:

1.  Stop all platform instances, if they are running.
1.  Provide usage flags for importing the certificate, at least `DigitalSignature` and `KeyEncipherment`.
1.  Prepare two certificate files:
    
    * A public security certificate file (*.CRT).        
    * A security certificate file with a private key and intermediate trust info (*.PFX, PKCS#12).
        
1.  Set the configuration options (via **appsettings.json** or environment variables) as follows:
    
	* **Auth:PublicCertPath**: Path to the *.CRT file.   
    * **Auth:PrivateKeyPath**: Path to the *.PFX file.   
	* **Auth:PrivateKeyPassword**: Plaintext password from the private part of the PFX certificate.
        
1.  Run the platform. The system will save the certificates in the database at startup.

!!! note
	You can delete certificate files and remove keys from the configuration for safety reason.

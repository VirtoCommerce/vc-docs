
To protect the tokens it issues, Virto Commerce uses the **encryption credentials to ensure the content of tokens cannot read by malicious parties**. They can be either asymmetric (e.g, an RSA key) or symmetric.

### Using Self-signed Certificate

Self-signed certificate is generated and stored in the database at the first platform startup.
  
If you want to re-generate the certificate, just stop all the platform instances, and then clear the `ServerCertificate` table in the database and run the platform again.

### Registering Certificate (Recommended for Production-ready Scenarios)

To register a custom certificate, do the following:

1.  Stop all platform instances, if they are running.
    
2.  Provide usage flags for importing the certificate, at least `DigitalSignature` and `KeyEncipherment`.
    
3.  Prepare two certificate files:
    
    + Public security certificate file (*.CRT)
        
    + Security certificate file with private key and intermediate trust info (*.PFX, PKCS#12)
        
4.  Set the configuration options (through `appsettings.json` or environment variables) in the following way:
    
	+ **Auth:PublicCertPath**: Path to the *.CRT file
        
    + **Auth:PrivateKeyPath**: Path to the *.PFX file
        
	+ **Auth:PrivateKeyPassword**: Plaintext password from the private part of the PFX certificate
        
5.  Run the platform. The system will save the certificates in the database at startup.

!!! note
	You can delete certificate files and remove keys from the configuration for safety reason.

# PDF Generation

This guide provides step-by-step instructions to add support for PDF file generation within your application. By integrating HTML to PDF conversion tools, you can easily generate PDF files from HTML content.

To add support for PDF file generation:

1. Go to [WkHtmlToPdf website](https://wkhtmltopdf.org/downloads.html) to download and install the HTML to PDF conversion tool. Choose the appropriate package based on your operating system.
  
1. Configure process start settings. Ensure the correct settings are configured for starting the conversion tool process. Example settings can be found in `VirtoCommerce.OrdersModule.Tests.ProcessHelperIntegrationTests`.

1. Start the conversion tool process. For example:

     ```cmd
     "c:\Program Files\wkhtmltopdf\bin\wkhtmltopdf" --dpi 300 --page-size A4 --encoding "utf-8" --viewport-size "1920x1080" input.html output.pdf   
     ```


![Readmore](media/readmore.png){: width="25"} [WkHtmlToPdf manual](https://wkhtmltopdf.org/index.html)

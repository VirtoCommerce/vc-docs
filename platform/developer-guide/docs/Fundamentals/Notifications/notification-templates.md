# Notification Templates

Although users can [modify or define notification templates through Platform Manager](https://docs.virtocommerce.org/new/user-guide/notifications/notification-templates), in real environments, it is more convenient to declare and store the notification templates under the source code control along with the main code of the module’s solution. This method has the following advantages:

+ You can see and control all change history
    
+ You get more streamlined process for template distribution across multiple environments, e.g., development and production, without any need to work with templates stored in a database.

There are two ways to declare and distribute predefined notification templates through code:

+ As content files in `.csproj` of a custom module (preferred)
    
+ As inline definition in the source code
    

## Content Files in `.csproj`

Your first step is to create the *Templates* folder in the module solution:

```
ModuleWeb
├── Templates
    ├── SampleEmailNotification_body.en.html
    ├── SampleEmailNotification_subject.en.html
    └── SampleEmailNotification_sample.json
    
```

### Notification Naming Convention
Notification template files have the following naming convention:

`[NotificationTypeName]_[subject|body|sample][.lang?].[html|json]`, where:

+ `_subject.html` contains the content that will be rendered in the email subject
    
+ `_body.html` contains content that will be rendered in the email body
    
+ `_sample.json` contains the default JSON data that will be used for notification preview

+ `lang` is a two-letter language code; it is not required, and in case it is not provided, the template will be used by default for all requested languages, as long as the file for the required language is not found.

### Working with `.Web.csproj` File
Next, you need to edit the `.Web.csproj` file to allow all files from the *Templates* folder to be copied upon publishing. Technically, you need to add the following lines into `{Your module}.Web.csproj`:

```csharp title="{Your module}.Web.csproj"
 <ItemGroup>
        <NotificationTemplates Include="Templates/**" />
    </ItemGroup>
    <Target Name="CopyCustomContentOnPublish" AfterTargets="Publish">
        <Copy SourceFiles="@(NotificationTemplates)" DestinationFiles="$(PublishDir)\..\%(Identity)" />
    </Target>
```

The ***Notification*** module performs discovery for template files through the path managed by the `Notifications:DiscoveryPath` setting<!---TODO: link to setting in the configuration reference-->, which has the `Templates` value set by default.

In addition, if you want to use a different discovery path for individual notification types, you can add the following code in `Module.cs`:

```csharp title="module.cs" linenums="1"

public void PostInitialize(IApplicationBuilder appBuilder)
	{
	...
	var moduleTemplatesPath = Path.Combine(ModuleInfo.FullPhysicalPath, "Templates2");
	registrar.RegisterNotification<SampleEmailNotification>()
         .WithTemplatesFromPath(moduleTemplatesPath);
	...
	}
```

!!! note
	Through lines 4 and 5, you tell to the notification system to discover template files in the */Templates2* relative path for a notification with the `SampleEmailNotification` type.

## Inline Definition in Source Code

There is a less useful but still feasible way to define templates directly from the code:

```csharp
registrar.RegisterNotification<SampleEmailNotification>().WithTemplates(new EmailNotificationTemplate()
        {
            Subject = "Sample subject",
            Body = "<p>Sample text</p>",
        });
```

Alternatively, you can load what you need from the assembly embedded resources:

```csharp
var assembly = Assembly.GetExecutingAssembly();
registrar.RegisterNotification<SampleEmailNotification>().WithTemplates(new EmailNotificationTemplate()
        {
            Subject = assembly.GetManifestResourceStream("VirtoCommerce.NotificationsSampleModule.Web.Templates.SampleEmailNotification_subject.txt").ReadToString(),
            Body = assembly.GetManifestResourceStream("VirtoCommerce.NotificationsSampleModule.Web.Templates.SampleEmailNotification_body.html").ReadToString()
        });
```

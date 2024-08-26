# Health Checks in VirtoCommerce Platform

VirtoCommerce platform supports health checks through ASP.NET Core middlewares. To ensure robustness and reliability, this article covers two primary aspects:

* [Module health checks.](health-checks.md#module-health-checks)
* [Docker integration.](health-checks.md#docker-integration)

## Module health checks

To add health checks to your modules:

1. Create a class that inherits from the `IHealthCheck` interface and implement it. For example:

    ```csharp title="CatalogHealthCheck.cs"
    public class CatalogHealthCheck : IHealthCheck
    {
        public Task<HealthCheckResult> CheckHealthAsync(
            HealthCheckContext context,
            CancellationToken cancellationToken = default(CancellationToken))
        {
            var healthCheckResultHealthy = true;

            if (healthCheckResultHealthy)
            {
                return Task.FromResult(
                    HealthCheckResult.Healthy("A healthy result."));
            }

            return Task.FromResult(
                new HealthCheckResult(context.Registration.FailureStatus,
                "An unhealthy result."));
        }
    }
    ```

1. Register the created health checks in the service collection. For example, in your module's initialization:

    ```csharp title="Module.cs"
    public class Module : IModule
    {
        public void Initialize(IServiceCollection serviceCollection)
        {
            serviceCollection
                .AddHealthChecks()
                .AddCheck<CatalogHealthCheck>("catalog_health_check");

            // Other module initialization code here
        }
    }
    ```

Now you can check your platform by getting a response from `/health` endpoint:

![Health check](media/health-checks.png)

## Docker integration

For Docker environments, you can use the built-in `HEALTHCHECK` directive to monitor the status of your application. For example:

```bash
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit
```

![Readmore](media/readmore.png){: width="25"} [Microsoft ASP.NET Core Health Checks Documentation](https://docs.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-5.0)


# Installation and Deployment Options

There are two distinct concepts when bringing Virto Commerce online:

* **Installation**: The act of getting the Platform binaries onto a machine and making them runnable. Installation methods describe how the Platform is obtained and set up on the target machine.
* **Deployment**: The topology and environment where the Platform runs in production. Deployment topologies describe where the installed Platform runs and who operates the underlying infrastructure. Virto Commerce is a cloud-native platform that can be hosted across a range of topologies from a fully managed SaaS to sovereign, customer-isolated infrastructure.

You always pick one installation method and one deployment topology. For example, you might install from the CLI and deploy on Azure.

For a fast end-to-end trial that combines installation and deployment in one command, use [start-local](Installation-Guide/start-local.md). It is a turnkey path that does not combine with the other deployment topologies; the matrix below applies when you want to choose installation and deployment paths separately.

<table>
  <thead>
    <tr>
      <th>Step</th>
      <th>Type</th>
      <th>Option</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2">Installation</th>
      <td>Using precompiled binaries</td>
      <td>
        <a href="../Installation-Guide/windows#download-precompiled-binaries">Windows</a><br>
        <a href="../Installation-Guide/linux#download-precompiled-binaries">Linux</a><br>
        <a href="../Installation-Guide/macOS#download-precompiled-binaries">macOS</a>
      </td>
    </tr>
    <tr>
      <td>Using CLI</td>
      <td>
        <a href="../Installation-Guide/windows#use-virto-commerce-cli">Windows</a><br>
        <a href="../Installation-Guide/linux#use-virto-commerce-cli">Linux</a><br>
        <a href="../Installation-Guide/macOS#use-virto-commerce-cli">macOS</a>
      </td>
    </tr>
    <tr>
      <th rowspan="10">Deployment</th>
      <td>Managed PaaS<br>Vendor-hosted</td>
      <td><a href="https://docs.virtocommerce.org/platform/deployment-on-cloud/deploy-on-virto-cloud/">Virto Cloud</a></td>
    </tr>
    <tr>
      <td rowspan="3">Public cloud<br>Self-managed</td>
      <td><a href="../../Tutorials-and-How-tos/How-tos/deploy-platform-on-azure">Azure</a></td>
    </tr>
    <tr>
      <td><a href="../../Tutorials-and-How-tos/How-tos/deploy-platform-on-aws">AWS</a></td>
    </tr>
    <tr>
      <td><a href="../../Tutorials-and-How-tos/How-tos/deploy-platform-on-gcp">Google Cloud</a></td>
    </tr>
    <tr>
      <td rowspan="2">Private cloud<br>Isolated infra</td>
      <td>Single-tenant</td>
    </tr>
    <tr>
      <td>VPC isolation</td>
    </tr>
    <tr>
      <td rowspan="2">Government<br>Sovereign cloud</td>
      <td>Azure Government</td>
    </tr>
    <tr>
      <td>AWS GovCloud</td>
    </tr>
    <tr>
      <td rowspan="2">Containerized</td>
      <td><a href="../Installation-Guide/start-local">Docker (start-local)</a></td>
    </tr>
    <tr>
      <td>Kubernetes</td>
    </tr>
  </tbody>
</table>


<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../system-requirements">← System requirements</a>
    <a href="../Installation-Guide/windows">Installation on Windows →</a>
</div>
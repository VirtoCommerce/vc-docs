# Extend Main Menu

As part of extending the main menu, you can add new items to the application menu to enhance functionality and user access. Use this code to add new menu items:

```JS
.run(
  ['$rootScope', 'platformWebApp.mainMenuService', '$state', function ($rootScope, mainMenuService, $state) {
    //Register module in main menu
    var menuItem = {
      path: 'browse/unmanaged module',
      icon: 'fa fa-cube',
      title: 'My cool module',
      priority: 110,
      state: function () { $state.go('workspace.unmanagedModuleTemplate'); },
      permission: 'UnmanagedModulePermission'
    };
    mainMenuService.addMenuItem(menuItem);
  }]);
```

!!! note
	The `priority` property defines the menu position relative to the other menu options. **A smaller number means a higher priority**, and such a menu item will be displayed first.

<br>
<br>
********

<div style="display: flex; justify-content: space-between;">
    <a href="../../localization">← Countries management and localization</a>
    <a href="../blades-and-navigation">Blades and navigation →</a>
</div>
# Understanding VC-Shell Application Layout

VC-Shell applications follow a consistent and predictable layout structure, designed to provide a seamless user experience. This guide outlines the main components of this layout and their typical functions. The root of this layout is often managed by the `VcApp` UI component.

## Main Layout Components

### `VcApp` - The Root Container

*   **Description:** The `VcApp` component typically serves as the main container for the entire application. It provides the overall structure, including slots for the sidebar, app bar, and main content area.
*   **Key Component:** [`VcApp`](./ui-components/vc-app.md)

![App Layout](/platform/developer-guide/latest/custom-apps-development/media/app-layout.png)
![App Layout](/platform/developer-guide/latest/custom-apps-development/media/app-layout2.png)

### Sidebar (Main Navigation Menu & Integrated App Bar Elements)

*   **Description:** Usually located on the left side of the application, the sidebar is the primary hub for navigation and key application-level actions. It's often initially collapsed, showing a "burger" icon (☰). When expanded (by clicking the burger icon), it reveals:
    *   **Main Navigation Menu:** Contains links to different modules and top-level sections of the application. Menu items can have icons, labels, and can be organized into groups. (Managed by `useMenuService`)
    *   **Integrated App Bar Elements:** Within the expanded sidebar, typically at the top or bottom, elements traditionally found in an app bar are present. These include:
        *   **Application Title/Logo:** Branding and identification.
        *   **App Switcher:** (If multiple VC-Shell apps are configured) Allows users to switch between different applications. (Managed by `useAppSwitcher`)
        *   **User Dropdown Menu:** Provides access to user-specific actions like "Profile", "Change Password", "Theme Selector", and "Logout".
        *   **Notification Center:** An icon that indicates new notifications and allows access to the notification list. (Managed by `useNotifications`)
        *   **App Bar Widgets:** Custom widgets can be added here for quick access to information or actions. (Managed by `useAppBarWidget`)
        *   **Settings Menu:** Often accessed via the User Dropdown or a dedicated icon within this area, providing access to application settings. (Managed by `useSettingsMenu`)

*   **Key Composables/Services:** `useMenuService`, `useAppSwitcher`, `useNotifications`, `useAppBarWidget`, `useSettingsMenu`.

![App Layout](/platform/developer-guide/latest/custom-apps-development/media/app-layout3.gif)


*   **Further Reading:**
    *   [Building Navigation Menus with useMenuService](./Usage-Guides/building-navigation-menus-with-usemenuservice.md)
    *   [Customizing Notifications](./Usage-Guides/customizing-notifications.md)
    *   [Adding App Bar Widgets with useAppBarWidget](./Usage-Guides/adding-app-bar-widgets-with-useappbarwidget.md)
    *   [Managing Settings Menu with useSettingsMenu](./Usage-Guides/managing-settings-menu-with-usesettingsmenu.md)

### Main Content Area / Blade Navigation Area

*   **Description:** This is the largest area of the application, occupying the central space. It's where primary content, pages, and blades are displayed. When `VcBladeNavigation` is used, this area will render the stack of open blades.
*   **Key Component:** `VcBladeNavigation` is often used here to manage and display blades.

![App Layout](/platform/developer-guide/latest/custom-apps-development/media/app-layout4.png)

*   **Further Reading:**
    *   [Understanding Blade Anatomy](./Usage-Guides/understanding-blade-anatomy.md)
    *   [Working with Blade Navigation](./Usage-Guides/working-with-blade-navigation.md)
    *   [`VcBladeNavigation`](./shared/components/blade-navigation.md)

## How Layout Elements are Populated

Many of these layout elements are populated dynamically:

*   **Main Menu:** Module `defineOptions` (specifically the `menuItems` property) contribute to the main navigation menu, processed by `useMenuService`.
*   **App Bar Widgets (within Sidebar):** Registered using `useAppBarWidget().registerWidget()`.
*   **Settings Menu Items:** Registered using `useSettingsMenu().addSettingsMenuItem()`.
*   **Blades:** Opened programmatically using `useBladeNavigation().openBlade()` or via declarative links.

## Conclusion

Understanding the standard layout of a VC-Shell application helps in consistently placing features and information. Developers should leverage the provided composables and UI components (`VcApp`, `VcBladeNavigation`, etc.) to build applications that feel familiar and intuitive to users accustomed to the VC-Shell environment. Refer to the specific guides for each composable or component for detailed implementation. 

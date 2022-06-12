import type { MenuProps } from "antd";
import { Menu } from "antd";
import { Layout } from "antd";

import {
  DatabaseFilled,
  ClockCircleFilled,
  CalendarFilled,
  CheckSquareFilled,
  DeleteFilled,
} from "@ant-design/icons";

type MenuItem = Required<MenuProps>["items"][number];

function getItem(
  label: React.ReactNode,
  key: React.Key,
  icon?: React.ReactNode,
  children?: MenuItem[],
  type?: "group"
): MenuItem {
  return {
    key,
    icon,
    children,
    label,
    type,
  } as MenuItem;
}

const items: MenuProps["items"] = [
  getItem("All", "1", <DatabaseFilled />),
  getItem("Today", "2", <ClockCircleFilled />),
  getItem("Next 7 Days", "3", <CalendarFilled />),
  getItem("Completed", "4", <CheckSquareFilled />),
  getItem("Trash", "5", <DeleteFilled />),
];
const SideMenu = () => (
  <Menu
    onClick={() => console.log("clicked")}
    defaultSelectedKeys={["1"]}
    defaultOpenKeys={["sub1"]}
    mode="inline"
    items={items}
  />
);
export default SideMenu;

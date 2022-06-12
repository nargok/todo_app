import React from "react";
import logo from "./logo.svg";
import { Button } from "antd";
import { Typography } from "antd";
import { Layout } from "antd";

import TaskForm from "./components/TaskForm";

import "./App.css";
import SideMenu from "./components/SideMenu";

const { Header, Footer, Sider, Content } = Layout;

// const { Title } = Typography;

function App() {
  return (
    <div className="App">
      <Layout className="top">
        {/* <Header>Header</Header> */}
        <Layout>
          <Sider>
            <SideMenu />
          </Sider>
          <Content>Content</Content>
          <TaskForm></TaskForm>
        </Layout>
        {/* <Footer>Footer</Footer> */}
      </Layout>
    </div>
  );
}

export default App;

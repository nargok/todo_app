import { Typography } from "antd";
const { Title } = Typography;

type Props = {
  title: string;
};

const Header: React.FC<Props> = ({ title }) => (
  <>
    <Title level={2}>{title}</Title>　
  </>
);

export default Header;

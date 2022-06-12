import Header from "./Header";
import styled from "styled-components";

type Props = {
  listTitle?: string;
};

const TaskListIndex: React.FC<Props> = ({ listTitle = "All" }) => (
  <Container>
    <Header title={listTitle} />
  </Container>
);

export default TaskListIndex;

const Container = styled.div`
  padding: 16px;
`;

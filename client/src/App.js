// import { PrettyChatWindow } from 'react-chat-engine-pretty';

// const ChatsPage = () => {
//   return (
//     <div style={{ height: "100vh" }}>
//       <PrettyChatWindow
//         projectId="ad79d188-c853-40b7-8fa1-a8350e5facac"
//         username="zakezone"
//         secret="pass1234"
//         style={{ height: "100%" }}
//       />
//     </div>
//   );
// }

// export default ChatsPage;

import { useState } from "react";

import AuthPage from "./authPage";
import ChatsPage from "./chatsPage";

function App() {
  const [user, setUser] = useState();

  if (!user) {
    return <AuthPage onAuth={(user) => setUser(user)} />;
  } else {
    return <ChatsPage user={user} />;
  }
}

export default App;
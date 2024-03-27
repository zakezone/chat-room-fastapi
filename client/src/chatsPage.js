import React from 'react';

import { PrettyChatWindow } from "react-chat-engine-pretty";

const ChatsPage = (props) => {
    return (
        <div style={{ height: "100vh" }}>
            <PrettyChatWindow
                projectId="ae6e42f5-dafd-49fb-8524-3d6fa9bf2077"
                username={props.user.username}
                secret={props.user.secret} 
                style={{ height: "100vh" }}
            />
        </div>
    );
};

export default ChatsPage;
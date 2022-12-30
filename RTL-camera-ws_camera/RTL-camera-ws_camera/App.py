import React, { useState, useEffect } from "react";
import io from "socket.io-client";

const SERVER_IP = "http://65.1.162.104:3000";

function App() {
  const [connectionStatus, setConnectionStatus] = useState("Connected");

  const sio = io(SERVER_IP, {
    autoConnect: false,
  });

  useEffect(() => {
    sio.on("disconnect", () => {
      setConnectionStatus("Disconnected");
      sio.disconnect();
      reconnectsio();
    });
  }, [sio]);

  function reconnectsio() {
    sio.connect();
  }

  return (
    <div>
      <p>Connection Status: {connectionStatus}</p>
    </div>
  );
}

export default App;

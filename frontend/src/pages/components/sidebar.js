import React from "react";


import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";

export const SidebarData = [
  {
    title: "Questions",
    path: "/questions",
    icon: <AiIcons.AiFillHome />,
    cName: "nav-text"
  },
  {
    title: "Answers",
    path: "/answers",
    icon: <IoIcons.IoIosPaper />,
    cName: "nav-text"
  },
];

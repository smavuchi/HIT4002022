// import
import Dashboard from "views/Dashboard/Dashboard";
import MyAPIs from "views/Dashboard/MyAPIs";
import Tables from "views/Dashboard/Tables";
import Billing from "views/Dashboard/Billing";
import Profile from "views/Dashboard/Profile";
import SignIn from "views/Auth/SignIn.js";
import SignUp from "views/Auth/SignUp.js";

import Explore from "views/Dashboard/Explore";
import Subscriptions from "views/Dashboard/Subscriptions";
import Console from "views/Dashboard/Console";

import {
  HomeIcon,
  StatsIcon,
  CreditIcon,
  PersonIcon,
  DocumentIcon,
  RocketIcon,
  SupportIcon,
  GlobeIcon,
  WalletIcon
} from "components/Icons/Icons";

var dashRoutes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    rtlName: "لوحة القيادة",
    icon: <HomeIcon color="inherit" />,
    component: Dashboard,
    layout: "/admin",
  },
  {
    path: "/apis/mine",
    name: "My APIs",
    rtlName: "لوحة القيادة",
    icon: <StatsIcon color="inherit" />,
    component: MyAPIs,
    layout: "/admin",
  },
  {
    path: "/apis/subscriptions",
    name: "Subscriptions",
    rtlName: "لوحة القيادة",
    icon: <WalletIcon color="inherit" />,
    component: Subscriptions,
    layout: "/admin",
  },
  {
    path: "/apis/explore",
    name: "Explore APIs",
    rtlName: "لوحة القيادة",
    icon: <GlobeIcon color="inherit" />,
    component: Explore,
    layout: "/admin",
  },
  {
    path: "/apis/console",
    name: "Console",
    rtlName: "لوحة القيادة",
    icon: <DocumentIcon color="inherit" />,
    component: Console,
    layout: "/admin",
  },
  {
    path: "/profile",
    name: "Profile",
    rtlName: "لوحة القيادة",
    icon: <PersonIcon color="inherit" />,
    secondaryNavbar: true,
    component: Profile,
    layout: "/admin",
  },
  {
    path: "/signin",
    name: "Sign In",
    rtlName: "لوحة القيادة",
    icon: <DocumentIcon color="inherit" />,
    component: SignIn,
    layout: "/auth",
  },
  {
    path: "/signup",
    name: "Sign Up",
    rtlName: "لوحة القيادة",
    icon: <RocketIcon color="inherit" />,
    secondaryNavbar: true,
    component: SignUp,
    layout: "/auth",
  },
];
export default dashRoutes;

import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/NotFound";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import Header from "./components/Header";
import Home from "./pages/Home";
import Writeups from "./pages/Writeups";
import Proyectos from "./pages/Proyectos";
import Contacto from "./pages/Contacto";
import PostDetail from "./pages/PostDetail";

function Router() {
  return (
    <>
      <Header />
      <div className="pt-16 min-h-screen">
        <Switch>
          <Route path="/" component={Home} />
          <Route path="/writeups" component={Writeups} />
          <Route path="/proyectos" component={Proyectos} />
          <Route path="/contacto" component={Contacto} />
          <Route path="/noticias/:slug">
            {() => <PostDetail category="noticias" />}
          </Route>
          <Route path="/writeups/:slug">
            {() => <PostDetail category="writeups" />}
          </Route>
          <Route path="/proyectos/:slug">
            {() => <PostDetail category="proyectos" />}
          </Route>
          <Route path="/404" component={NotFound} />
          <Route component={NotFound} />
        </Switch>
      </div>
    </>
  );
}

function App() {
  return (
    <ErrorBoundary>
      <ThemeProvider defaultTheme="dark">
        <TooltipProvider>
          <Toaster />
          <Router />
        </TooltipProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}

export default App;

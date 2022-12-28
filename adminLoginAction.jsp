<%
    String username = request.getParameter("username");
    String password = request.getParameter("password");
    
    if("Arihant".equals(username) && "A@jain".equals(password))
    {
        response.sendRedirect("home.jsp");
    }
    else
    {
        response.sendRedirect("adminLogin.jsp?msg=invalid");
    }
    %>
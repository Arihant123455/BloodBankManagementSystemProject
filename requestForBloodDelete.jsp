<%@page import="java.sql.*"%>
<%@page import="Project.ConnectionProvider"%>
<%
    String mobilenumber = request.getParameter("mobilenumber");
    
    try
    {
        Connection con = ConnectionProvider.getCon();
        Statement st = con.createStatement();
        st.executeUpdate("delete from bloodrequest where mobilenumber='"+mobilenumber+"'");
        response.sendRedirect("requestForBlood.jsp");
    }
    catch(Exception e)
    {
         response.sendRedirect("requestForBlood.jsp");
    }
    %>
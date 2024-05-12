<?php
session_start();

session_unset();
session_destroy();

header("Location: loginregister.html");
exit;
?>
<script>
    alert("회원가입이 완료되었습니다");
    location.href = "loginregister.html";
</script>

      SUBROUTINE fg(o,n,i,j,t)
cf2py intent(inplace) o
cf2py intent(hide) n
      DOUBLE PRECISION o(n,n), t, c, s
      INTEGER i,j,k,n
      
        c = dcos(theta)
        s = dsin(theta)
        
        do k=1,n
            o(i,k) = o(i,k)*c + o(j,k)*s
            o(j,k) = o(j,k)*c - o(i,k)*s
        end do
      
      RETURN
      END
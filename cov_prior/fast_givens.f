      SUBROUTINE fg(o,oc,n,i,j,t)
cf2py intent(inplace) oc
cf2py intent(hide) n
      DOUBLE PRECISION o(n,n), oc(n,n), t, c, s
      INTEGER i,j,k,n
      
        c = dcos(t)
        s = dsin(t)
        
        
        do k=1,n
            oc(i,k) = o(i,k)*c + o(j,k)*s
            oc(j,k) = o(j,k)*c - o(i,k)*s
        end do
      
      RETURN
      END
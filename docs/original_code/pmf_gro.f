      program pmf
c     Created by Higo
c     Modified by S.Ono 2001/09/06
c                       2002/07/19
c     
c     A main program for the best fit procedure.
c*******************************************************
c      include 'COMDAT.fit'
      implicit none

      integer nbinmx,nbinmx2,maxpcomp
      parameter (nbinmx=100000,nbinmx2=5000)
      parameter (maxpcomp=10)

      real*8  enebin(nbinmx),epdf(nbinmx)
      real*8  pcomp(maxpcomp)
      real*8  px,py,probsum(nbinmx2,nbinmx2)
      real*8  cminx,cminy,binx,biny,xgrid,ygrid
c      real*8  cminx,binx,cminy,biny
c      integer nxaxis,nyaxis,nxbinsize,nybinsize
      integer ncomp,nxaxis,nyaxis,nxbinsize,nybinsize
c****

      character aaa*6
      character endmark*3
      character*80 inppdf,inppca,outgrd,outplt
      real*8 caltemp

      integer i,ii,jj,ict,iimax,imin,imax,min,max
      integer nbin,npick
      real*8  pdfmx,prob1,ep,prob,e1,e2,px1,py1
      real*8  const,probsummin
      real*8  cmix,cmiy,cmax,cmay,cstep,cstep0

c**************************************
      print*," ********************************"
      print*," * Make a trajectory-like file  *"
      print*," * from a real trajectory file. *"
      print*," ********************************"
      print*,' This program generates an emsemble at a given'
      print*,' temperature, with using energy distribution'
      print*,' at the temperature.'
      print*,' '

      print*,'  *********************************'
      print*,'  * Input conformations.          *'
      print*,'  *********************************'
      print*,'  To draw energy landscape, the input confs. are'
      print*,'  judged by the energy pdf at a given temperature.'
      print*,' '

c      read(5,*) iotform

      read(5,*) ncomp
      read(5,*) nxaxis
      read(5,*) nyaxis
      read(5,*) cminx
      read(5,*) binx
      read(5,*) nxbinsize
      read(5,*) cminy
      read(5,*) biny
      read(5,*) nybinsize
      read(5,*) caltemp
      read(5,'(a80)') inppdf
      read(5,'(a80)') inppca
      read(5,'(a80)') outgrd
      read(5,'(a80)') outplt
      read(5,621) endmark
 621  format(a3)
      if(endmark.ne."END") then
         print*,' ????????????????'
         print*,' ? No end-mark. ?'
         print*,' ????????????????'
         print*,' endmark = ',endmark
         stop
      endif
c********
      print*,"  <input parameters>"

      print*," "

c      if(iotform.eq.1) then
c         print*,'  Output all atoms.'
c      endif
c      if(iotform.eq.2) then
c         print*,'  Output only peptide atoms.'
c      endif
c      print*," "

      print*,'  number of principal axes = ',ncomp
      print*," "
      print*,'  grid information  '
      print*,'  x axis = ',nxaxis,'th axis '
      print*,'  y axis = ',nyaxis,'th axis '
      print*,'  xgrid  '
      print*,'    min = ',cminx
      print*,'    binlength = ',binx
      print*,'    binsize = ',nxbinsize
      print*,'  ygrid  '
      print*,'    min = ',cminy
      print*,'    binlength = ',biny
      print*,'    binsize = ',nybinsize
      print*," "

 624  format('   control para. to pick up the conf. = ',f10.3)
      print*," "


CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
c     input energy pdf
      print*,' *********************************'
      print*,' * Input the energy pdf. (t_pdf) *'
      print*,' *********************************'
      print*,'  NOTE: The input energy pdf is given in a log scale.'
      print*,'        In this program, the scale is put back to the'
      print*,'        normal scale.'
      print*,' '
c**********
      ii=0

      open(unit=19,file=inppdf,status='old',err=9100)
 500  continue
      ii=ii+1

      if(ii.gt.nbinmx) then
         print*,' ????????????????????????????????'
         print*,' ? nbinmx is too small. (t_pdf) ?'
         print*,' ????????????????????????????????'
         stop
      endif

      read(19,*,end=990) enebin(ii),epdf(ii)
c     c        write(6,100) ii,enebin(ii),epdf(ii)
 100  format(i6,4x,e16.7,4x,e16.7)

      goto 500
 990  continue
      close(19)

      nbin=ii-1

      write(6,310) nbin
 310  format('  N of bins input = ',i6)
c**********
c     Normalization.

      pdfmx=-1.0e+10
      do ii=1,nbin
         if(epdf(ii).gt.pdfmx) then
            pdfmx=epdf(ii)
            iimax=ii
         endif
      enddo

      write(6,320) iimax,pdfmx
 320  format('  Maximun pdf = ',i6,4x,e16.7)
      print*,'     The pdf is normalized by the maximun above.'
      print*,' '

      do ii=1,nbin
         epdf(ii)=epdf(ii) - pdfmx
         epdf(ii)=exp(epdf(ii))
         if(epdf(ii).lt.1.e-11) epdf(ii)=0.0d0
c     c          write(6,100) ii,enebin(ii),epdf(ii)
      enddo
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

c************************
c     Input of quasi harmonic analysis data

      prob1=0d0
      do ii=1,nxbinsize
         do jj=1,nybinsize
            probsum(ii,jj)=0d0
         enddo
      enddo

      ict=0
      npick=0

c      infil=1
c      numfil=1

      open(unit=111,file=inppca,status='old', err=9200)
 888  continue

c      if(infil.eq.1) indev=111

c     Input a conf.

      ict=ict+1
      if(npick.eq.0) read(111,*) aaa
      read(111,'(F13.5,500F9.3)',end=121) 
     *     ep,(pcomp(ii),ii=1,ncomp)
      npick=npick+1
c     c        write(6,*) ep,(pcomp(ii),ii=1,ncomp)
c**** 
c     Judge output or not.

      prob=0.0d0
      do ii=2,nbin
         e1=enebin(ii-1)
         e2=enebin(ii)
         if(ep.ge.e1 .and. ep.lt.e2) then
            prob=epdf(ii)
            goto 575
         endif
      enddo

 575  continue

C     restore prob 
      prob1=prob1+prob
      px=pcomp(nxaxis)
      py=pcomp(nyaxis)

      if (px.lt.cminx.or.py.lt.cminy) goto 510
      px1=px-cminx
      py1=py-cminy
      ii=int(px1/binx)+1
      jj=int(py1/biny)+1
      if (ii.gt.nxbinsize.or.jj.gt.nybinsize) goto 510
      probsum(ii,jj)=probsum(ii,jj)+prob
 510  continue

      write(6,'(2f8.2,2i5,f20.15)') px,py,ii,jj,prob
      goto 888
 121  continue
      close(111)

      write(6,625) npick
 625  format('   pick up the conf. = ',i10)
      write (6,*) prob1

C     calc potential of mean force
c$$$      const=(1.380658d-23)*caltemp*(2.390057d-1)/1000d0
c$$$     +     *(6.022137d23)
      const=8.314462145d-3 * caltemp

      do ii=1,nxbinsize
         do jj=1,nybinsize
            if(probsum(ii,jj).ne.0d0) then
               probsum(ii,jj)=-1d0*const*log(probsum(ii,jj))
            endif
         enddo
      enddo

      probsummin=100000000d0
      do ii=1,nxbinsize
         do jj=1,nybinsize
            if (probsum(ii,jj).lt.probsummin) then
               probsummin=probsum(ii,jj)
            endif
         enddo
      enddo


      open(unit=60,file=outgrd,status='unknown', err=9300)
      do ii=1,nxbinsize
         do jj=1,nybinsize
            if(probsum(ii,jj).eq.0d0) then
               probsum(ii,jj)=50d0
            else
               probsum(ii,jj)=probsum(ii,jj)-probsummin
            endif
            xgrid=cminx+(ii-1)*binx+binx/2d0
            ygrid=cminy+(jj-1)*biny+biny/2d0
            write(60,'(2f10.3,f15.5)') xgrid,ygrid,probsum(ii,jj)
         enddo
         write(60,'(a1)') ' '
      enddo
      close(60)

      open(unit=61,file=outplt,status='unknown', err=9400)
      write(61,'(a14)') '$ DATA=CONTOUR'
      cmix=cminx+binx/2d0
      cmiy=cminy+biny/2d0
      cmax=cminx+(nxbinsize-1)*binx+binx/2d0
      cmay=cminy+(nybinsize-1)*biny+biny/2d0
      write(61,'(a7,f6.1,a6,f6.1)') '% xmin=',cmix,' xmax=',cmax
      write(61,'(a7,f6.1,a6,f6.1)') '% ymin=',cmiy,' ymax=',cmay
      write(61,'(a5,i2,a4,i2)') '% nx=',nxbinsize,' ny=',nybinsize
      cstep0=(cmax-cmix)/10.d0
      if (cstep0 .gt. 10.) then
         cstep=20.0
      elseif (cstep0 .gt. 5.) then
         cstep=10.0
      elseif (cstep0.gt.2.) then
         cstep=5.0
      elseif (cstep0.gt.0.5) then
         cstep=2.0
      else
         cstep=1.0
      endif
      min=int((cmix-cstep)/cstep)*cstep
      max=int((cmax+cstep)/cstep)*cstep
      do i=min,max,cstep
         write(61,2001) i,i
      enddo
 2001 format('% xticklabel= (',i4,',',i4,')')
      cstep0=(cmay-cmiy)/10.d0
      if (cstep0 .gt. 10.) then
         cstep=20.0
      elseif (cstep0 .gt. 5.) then
         cstep=10.0
      elseif (cstep0.gt.2.) then
         cstep=5.0
      elseif (cstep0.gt.0.5) then
         cstep=2.0
      else
         cstep=1.0
      endif
      imin=int((cmiy-cstep)/cstep)*cstep
      imax=int((cmay+cstep)/cstep)*cstep
      do i=imin,imax,cstep
         write(61,2002) i,i
      enddo
 2002 format('% yticklabel= (',i4,',',i4,')')
c      write(61,'(a23)') '% xticklabel= (-70,-70)'
c      write(61,'(a23)') '% xticklabel= (-60,-60)'
c      write(61,'(a23)') '% xticklabel= (-50,-50)'
c      write(61,'(a23)') '% xticklabel= (-40,-40)'
c      write(61,'(a23)') '% xticklabel= (-30,-30)'
c      write(61,'(a23)') '% xticklabel= (-20,-20)'
c      write(61,'(a23)') '% xticklabel= (-10,-10)'
c      write(61,'(a19)') '% xticklabel= (0,0)'
c      write(61,'(a21)') '% xticklabel= (10,10)'
c      write(61,'(a21)') '% xticklabel= (20,20)'
c      write(61,'(a21)') '% xticklabel= (30,30)'
c      write(61,'(a21)') '% xticklabel= (40,40)'
c      write(61,'(a21)') '% xticklabel= (50,50)'
c      write(61,'(a23)') '% yticklabel= (-60,-60)'
c      write(61,'(a23)') '% yticklabel= (-50,-50)'
c      write(61,'(a23)') '% yticklabel= (-40,-40)'
c      write(61,'(a23)') '% yticklabel= (-30,-30)'
c      write(61,'(a23)') '% yticklabel= (-20,-20)'
c      write(61,'(a23)') '% yticklabel= (-10,-10)'
c      write(61,'(a19)') '% yticklabel= (0,0)'
c      write(61,'(a21)') '% yticklabel= (10,10)'
c      write(61,'(a21)') '% yticklabel= (20,20)'
c      write(61,'(a21)') '% yticklabel= (30,30)'
c      write(61,'(a21)') '% yticklabel= (40,40)'
c      write(61,'(a21)') '% yticklabel= (50,50)'
      write(61,'(a22)') '% cmin= 0.0 cmax= 10.0'
      write(61,'(a12)') '% nsteps= 10'
      write(61,'(a10)') '% contfill'

      do ii=1,nybinsize
         write(61,'(5f15.5)') (probsum(jj,ii),jj=1,nxbinsize)
      enddo

      write(61,'(a1)') ' '
      write(61,'(a5)') '$ END'
      close(61)

      stop

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
 9100 write(*,*) 'Open error: inppdf',inppdf
      stop
 9200 write(*,*) 'Open error: inppca',inppca
      stop
 9300 write(*,*) 'Open error: outgrd',outgrd
      stop
 9400 write(*,*) 'Open error: outplt',outplt
      stop
      end


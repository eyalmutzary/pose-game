import Backdrop from '@/lib/components/Backdrop'
import { Button } from '@/lib/components/Button'
import Container from '@/lib/components/Container'
import LogoText from '@/lib/components/LogoText'

const Gameover = ({ score }: { score: number }) => {
  return (
    <>
    <div className='z-50 flex flex-col gap-6 w-fit'>
      <Container className="flex-col items-center justify-center p-5 text-center">
        <LogoText className="text-[4em]">Game Over</LogoText>
        <p className="mt-6 text-[2em]">
          You scored <strong>{score}</strong> points
        </p>
      </Container>
      <Button onClick={() => window.location.reload()}>Play Again</Button>
    </div>
      <Backdrop />
    </>
  )
}

export default Gameover

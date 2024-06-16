import Container from '@/lib/components/Container'
import PoseBox from './PoseBox'
import { Box } from '../page'

type PoseSliderProps = {
  boxes: {[id: number]: Box}
  removeBox: (id: number) => void
}

const PoseSlider = ({ boxes, removeBox }: PoseSliderProps) => {
  return (
    <Container className={`min-w-[80vw] flex relative overflow-hidden min-h-48`}>
      {Object.keys(boxes).map((id) => (
        <PoseBox key={Number(id)} id={Number(id)} removeBox={removeBox} {...boxes[Number(id)]} />
      ))}
    </Container>
  )
}

export default PoseSlider

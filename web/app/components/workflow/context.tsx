'use client'

import { createContext, useContext } from 'use-context-selector'
import type {
  Edge,
  ReactFlowInstance,
} from 'reactflow'
import type {
  BlockEnum,
  Node,
} from './types'

export type WorkflowContextValue = {
  mode: string
  reactFlow: ReactFlowInstance
  nodes: Node[]
  edges: Edge[]
  selectedNodeId?: string
  handleSelectedNodeIdChange: (nodeId: string) => void
  selectedNode?: Node
  handleAddNextNode: (prevNode: Node, nextNodeType: BlockEnum) => void
  handleUpdateNodeData: (nodeId: string, data: Node['data']) => void
}

export const WorkflowContext = createContext<WorkflowContextValue>({
  mode: 'workflow',
  reactFlow: null as any,
  nodes: [],
  edges: [],
  handleSelectedNodeIdChange: () => {},
  handleAddNextNode: () => {},
  handleUpdateNodeData: () => {},
})
export const useWorkflowContext = () => useContext(WorkflowContext)
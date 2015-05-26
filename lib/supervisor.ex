defmodule Snake.Supervisor do
  use Supervisor

  def start_link do
    Supervisor.start_link(__MODULE__, :ok,name: __MODULE__ )
  end


  def init(:ok) do
   
    pool_options = [
      name: {:local, :snake_pool},
      worker_module: Snake.Worker,
      size: 20,
      max_overflow: 60
    ]

    children = [
      :poolboy.child_spec(:snake_pool, pool_options, [])
    ]

    supervise(children, strategy: :one_for_all)


  end

end